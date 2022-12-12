import graphene

from ...blog import models
from ..core.connection import CountableConnection
from ..core.types.model import ModelObjectType


class Category(ModelObjectType):
    id = graphene.GlobalID(required=True)
    name = graphene.String(required=True)

    class Meta:
        model = models.Category


class CategoryCountableConnection(CountableConnection):
    class Meta:
        node = Category
