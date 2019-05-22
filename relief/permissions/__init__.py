from .regions import get_release_for_region


def get_queryset_for_user(queryset, user):
    return get_release_for_region(queryset, user)
