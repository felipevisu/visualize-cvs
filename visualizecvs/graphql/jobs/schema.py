import graphene

from ..core.connection import (create_connection_slice,
                               filter_connection_queryset)
from ..core.fields import FilterConnectionField
from .filters import JobFilterInput
from .mutations import CVCreate
from .resolvers import resolve_job_by_name, resolve_jobs
from .sorters import JobSortingInput
from .types import Job, JobCountableConnection


class Query(graphene.ObjectType):
    jobs = FilterConnectionField(
        JobCountableConnection,
        filter=JobFilterInput(),
        sort_by=JobSortingInput(),
    )
    job = graphene.Field(
        Job, 
        id=graphene.Argument(graphene.ID), 
        name=graphene.Argument(graphene.String)
    )

    @staticmethod
    def resolve_job(_root, _info, *, id=None, name=None):
        if id:
            return None
        if name:
            return resolve_job_by_name(name=name)

    @staticmethod
    def resolve_jobs(_root, info, **kwargs):
        qs = resolve_jobs()
        qs = filter_connection_queryset(qs, kwargs)
        return create_connection_slice(qs, info, kwargs, JobCountableConnection)


class Mutation(graphene.ObjectType):
    cv_create = CVCreate.Field()