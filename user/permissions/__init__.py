def get_queryset_for_user(queryset, user):
    if not user.is_superuser:
        queryset = queryset.filter(profile__organization=user.profile.organization)
    return queryset
