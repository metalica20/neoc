import django_filters
from .models import Release
from incident.models import Incident
from loss.models import People


class ReleaseFilter(django_filters.FilterSet):
    incident = django_filters.ModelMultipleChoiceFilter(
        queryset=Incident.objects.all(),
        lookup_expr='in',
        widget=django_filters.widgets.CSVWidget,
    )
    person = django_filters.ModelMultipleChoiceFilter(
        queryset=People.objects.all(),
        lookup_expr='in',
        widget=django_filters.widgets.CSVWidget,
    )

    class Meta:
        model = Release
        fields = ['incident', 'person']
