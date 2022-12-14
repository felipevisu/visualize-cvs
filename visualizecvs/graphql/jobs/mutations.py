import graphene

from ...jobs import models
from ..core.mutations import ModelMutation
from ..core.types.common import NonNullList, Upload
from .types import CV
from .utils import send_cv_email


class CVInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    email = graphene.String(required=True)
    phone = graphene.String(required=True)
    city = graphene.String(required=True)
    academic_experience = graphene.String()
    professional_experience = graphene.String()
    social_links = graphene.String()
    file = Upload()
    jobs = NonNullList(graphene.ID)


class CVCreate(ModelMutation):
    cv = graphene.Field(CV)

    class Arguments:
        input = CVInput(required=True)

    class Meta:
        model = models.CV
        object_type = CV

    @classmethod
    def perform_mutation(cls, _root, info, **data):
        input = data.get("input")
        instance = models.CV()

        cleaned_input = cls.clean_input(info, instance, input)
        instance = cls.construct_instance(instance, cleaned_input)

        cls.clean_instance(info, instance)
        instance.save()

        cls._save_m2m(info, instance, cleaned_input)
        send_cv_email(instance)
        return CVCreate(cv=instance)