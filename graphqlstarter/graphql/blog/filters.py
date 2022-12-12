import django_filters
from django.db.models import Q

from ...blog.models import Category
from ..core.filters import GlobalIDMultipleChoiceFilter
from ..core.types import FilterInputObjectType


class CategoryFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method="category_filter_search")
    ids = GlobalIDMultipleChoiceFilter(field_name="id")

    class Meta:
        model = Category
        fields = ["search"]

    @classmethod
    def category_filter_search(cls, queryset, _name, value):
        if not value:
            return queryset

        return queryset.filter(Q(name__icontains=value))


class CategoryFilterInput(FilterInputObjectType):
    class Meta:
        filterset_class = CategoryFilter
