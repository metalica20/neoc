from .ministry import get_queryset_for_ministry
from .police import get_queryset_for_police
from .regions import get_queryset_for_region


def get_queryset_for_user(queryset, user):
    queryset = get_queryset_for_police(queryset, user)
    queryset = get_queryset_for_ministry(queryset, user)
    queryset = get_queryset_for_region(queryset, user)
    return queryset.distinct()
