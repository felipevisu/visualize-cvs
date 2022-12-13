import graphene

from ..core.types.sort_input import SortInputObjectType


class JobSortField(graphene.Enum):
    NAME = ["name"]


class JobSortingInput(SortInputObjectType):
    class Meta:
        sort_enum = JobSortField
        type_name = "jobs"
