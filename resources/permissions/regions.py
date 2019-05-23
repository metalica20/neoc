def get_queryset_for_region(queryset, user):
    region = user.profile.region
    if region == user.profile.MUNICIPALITY:
        queryset = queryset.filter(
            ward__municipality=user.profile.municipality
        )
    if region == user.profile.DISTRICT:
        queryset = queryset.filter(
            ward__municipality__district=user.profile.district
        )
    if region == user.profile.PROVINCE:
        queryset = queryset.filter(
            ward__municipality__district__province=user.profile.province
        )
    return queryset
