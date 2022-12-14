import graphene

from ...jobs import models
from ..core.mutations import ModelMutation
from ..core.types.common import NonNullList, Upload
from .types import CV


class CVInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    email = graphene.String(required=True)
    phone = graphene.String(required=True)
    city = graphene.String(required=True)
    academic_experience = graphene.String()
    professional_experience = graphene.String()
    instagram = graphene.String()
    facebook = graphene.String()
    linkedin = graphene.String()
    behance = graphene.String()
    portfolio_url = graphene.String()
    file = Upload()
    jobs = NonNullList(graphene.ID)


class CVCreate(ModelMutation):
    cv = graphene.Field(CV)

    class Arguments:
        input = CVInput(required=True)

    class Meta:
        model = models.CV
        object_type = CV