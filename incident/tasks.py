import datetime
from celery import shared_task
from django.core.cache import cache


@shared_task
def update_lnd(func, request, *args, **kwargs):
    lifetime = 60*60*8
    now = datetime.datetime.now()
    response = func(request, *args, **kwargs).render()
    cache.set(
        request.GET.urlencode(),
        (response, now + datetime.timedelta(seconds=lifetime)),
        60*60*24*7
    )
