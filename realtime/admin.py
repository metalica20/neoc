from django.contrib import admin
from .models import (
    Earthquake,
    River,
    Rain,
    Fire,
)


admin.site.register([Earthquake, River, Rain, Fire])
