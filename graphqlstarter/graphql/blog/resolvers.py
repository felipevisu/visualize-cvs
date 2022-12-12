from ...blog import models


def resolve_category_by_name(name):
    return models.Category.objects.filter(name=name).first()

def resolve_categories():
    return models.Category.objects.all()
