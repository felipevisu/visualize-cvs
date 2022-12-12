import binascii
from enum import Enum
from typing import Type, Union
from uuid import UUID

import graphene
from graphene import ObjectType
from graphql.error import GraphQLError


def validate_if_int_or_uuid(id):
    result = True
    try:
        int(id)
    except ValueError:
        try:
            UUID(id)
        except (AttributeError, ValueError):
            result = False
    return result
    

def from_global_id_or_error(
    id: str, only_type: Union[ObjectType, str, None] = None, field: str = "id"
):
    try:
        _type, _id = graphene.Node.from_global_id(id)
    except (binascii.Error, UnicodeDecodeError, ValueError):
        raise GraphQLError(f"Couldn't resolve id: {id}.")

    if only_type and str(_type) != str(only_type):
        raise GraphQLError(f"Must receive a {only_type} id.")
    return _type, _id

