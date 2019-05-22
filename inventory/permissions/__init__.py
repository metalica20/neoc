from .regions import get_queryset_for_region


def get_queryset_for_user(queryset, user):
    return get_queryset_for_region(queryset, user)
