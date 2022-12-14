import graphene

from .jobs.schema import Mutation as JobMutation
from .jobs.schema import Query as JobQuery


class Query(
    JobQuery
):
    pass



class Mutation(
    JobMutation
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
