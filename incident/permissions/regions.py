# filter incidents and loss by user regions
def get_queryset_for_region(queryset, user):
    region = user.profile.region
    if region == user.profile.MUNICIPALITY:
        queryset = queryset.filter(
            wards__municipality=user.profile.municipality
        )
    if region == user.profile.DISTRICT:
        queryset = queryset.filter(
            wards__municipality__district=user.profile.district
        )
    if region == user.profile.PROVINCE:
        queryset = queryset.filter(
            wards__municipality__district__province=user.profile.province
        )
    return queryset
