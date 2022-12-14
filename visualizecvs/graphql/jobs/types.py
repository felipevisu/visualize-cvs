import graphene

from ...jobs import models
from ..core.connection import CountableConnection
from ..core.types.common import File, NonNullList
from ..core.types.model import ModelObjectType


class Job(ModelObjectType):
    id = graphene.GlobalID(required=True)
    name = graphene.String(required=True)


    class Meta:
        model = models.Job


class JobCountableConnection(CountableConnection):
    class Meta:
        node = Job


class CV(ModelObjectType):
    id = graphene.GlobalID(required=True)
    name = graphene.String(required=True)
    email = graphene.String(required=True)
    phone = graphene.String(required=True)
    city = graphene.String(required=True)
    academic_experience = graphene.String()
    professional_experience = graphene.String()
    social_links = graphene.String()
    file = graphene.Field(File)
    jobs = NonNullList(lambda: Job)

    class Meta:
        model = models.CV


class CVCountableConnection(CountableConnection):
    class Meta:
        node = CV