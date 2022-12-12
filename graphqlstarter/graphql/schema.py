import graphene

from .blog.schema import Query as BlogQuery


class Query(
    BlogQuery
):
    pass


schema = graphene.Schema(query=Query)
