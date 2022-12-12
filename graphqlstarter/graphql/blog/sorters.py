import graphene

from ..core.types.sort_input import SortInputObjectType


class CategorySortField(graphene.Enum):
    NAME = ["name"]


class CategorySortingInput(SortInputObjectType):
    class Meta:
        sort_enum = CategorySortField
        type_name = "categories"
