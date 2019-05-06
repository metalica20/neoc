# filter incidents and loss for police
def get_queryset_for_police(queryset, user):
    if user.groups.filter(name='Nepal Police').exists():
        return queryset.filter(source__name='nepal_police')
    return queryset
