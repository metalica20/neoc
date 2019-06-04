from .regions import get_queryset_for_region


def get_queryset_for_user(queryset, user):
    # isn't used for now as police can see all incidents
    # queryset = get_queryset_for_police(queryset, user)
    queryset = get_queryset_for_region(queryset, user)
    return queryset.distinct()
