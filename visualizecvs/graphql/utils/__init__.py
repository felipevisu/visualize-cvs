from typing import Union
from uuid import UUID

import graphene
from django.db.models import Q
from graphql.error import GraphQLError

from ..core.utils import from_global_id_or_error

ERROR_COULD_NO_RESOLVE_GLOBAL_ID = (
    "Could not resolve to a node with the global id list of '%s'."
)
REVERSED_DIRECTION = {
    "-": "",
    "": "-",
}


def resolve_global_ids_to_primary_keys(
    ids, graphene_type=None, raise_error: bool = False
):
    pks = []
    invalid_ids = []
    used_type = graphene_type

    for graphql_id in ids:
        if not graphql_id:
            invalid_ids.append(graphql_id)
            continue

        try:
            node_type, _id = from_global_id_or_error(graphql_id)
        except Exception:
            invalid_ids.append(graphql_id)
            continue

        # Raise GraphQL error if ID of a different type was passed
        if used_type and str(used_type) != str(node_type):
            if not raise_error:
                continue
            raise GraphQLError(f"Must receive {str(used_type)} id: {graphql_id}.")

        used_type = node_type
        pks.append(_id)

    if invalid_ids:
        raise GraphQLError(ERROR_COULD_NO_RESOLVE_GLOBAL_ID % invalid_ids)

    return used_type, pks


def _resolve_graphene_type(schema, type_name):
    type_from_schema = schema.get_type(type_name)
    if type_from_schema:
        return type_from_schema.graphene_type
    raise GraphQLError("Could not resolve the type {}".format(type_name))


def get_nodes(
    ids,
    graphene_type: Union[graphene.ObjectType, str, None] = None,
    model=None,
    qs=None,
    schema=None,
):
    """Return a list of nodes.

    If the `graphene_type` argument is provided, the IDs will be validated
    against this type. If the type was not provided, it will be looked up in
    the schema. Raises an error if not all IDs are of the same
    type.

    If the `graphene_type` is of type str, the model keyword argument must be provided.
    """
    nodes_type, pks = resolve_global_ids_to_primary_keys(
        ids, graphene_type, raise_error=True
    )
    # If `graphene_type` was not provided, check if all resolved types are
    # the same. This prevents from accidentally mismatching IDs of different
    # types.
    if nodes_type and not graphene_type:
        if schema:
            graphene_type = _resolve_graphene_type(schema, nodes_type)
        else:
            raise GraphQLError("GraphQL schema was not provided")

    if qs is None and graphene_type and not isinstance(graphene_type, str):
        qs = graphene_type._meta.model.objects
    elif model is not None:
        qs = model.objects

    nodes = list(qs.filter(pk__in=pks)) if qs else []
    nodes.sort(key=lambda e: pks.index(str(e.pk)))  # preserve order in pks

    if not nodes:
        raise GraphQLError(ERROR_COULD_NO_RESOLVE_GLOBAL_ID % ids)

    nodes_pk_list = [str(node.pk) for node in nodes]
    for pk in pks:
        assert pk in nodes_pk_list, "There is no node of type {} with pk {}".format(
            graphene_type, pk
        )
    return nodes


def _get_node_for_types_with_double_id(qs, pks, graphene_type):
    uuid_pks = []
    old_pks = []
    is_order_type = str(graphene_type) == "Order"

    for pk in pks:
        try:
            uuid_pks.append(UUID(str(pk)))
        except ValueError:
            old_pks.append(pk)
    if is_order_type:
        lookup = Q(id__in=uuid_pks) | (Q(use_old_id=True) & Q(number__in=old_pks))
    else:
        lookup = Q(id__in=uuid_pks) | (Q(old_id__isnull=False) & Q(old_id__in=old_pks))
    nodes = list(qs.filter(lookup))
    old_id_field = "number" if is_order_type else "old_id"
    return sorted(
        nodes,
        key=lambda e: pks.index(
            str(e.pk) if e.pk in uuid_pks else str(getattr(e, old_id_field))
        ),
    )  # preserve order in pks