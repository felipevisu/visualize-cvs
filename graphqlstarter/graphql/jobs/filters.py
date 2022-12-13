import django_filters
from django.db.models import Q

from ...jobs.models import Job
from ..core.filters import GlobalIDMultipleChoiceFilter
from ..core.types import FilterInputObjectType


class JobFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method="job_filter_search")
    ids = GlobalIDMultipleChoiceFilter(field_name="id")

    class Meta:
        model = Job
        fields = ["search"]

    @classmethod
    def job_filter_search(cls, queryset, _name, value):
        if not value:
            return queryset

        return queryset.filter(Q(name__icontains=value))


class JobFilterInput(FilterInputObjectType):
    class Meta:
        filterset_class = JobFilter
