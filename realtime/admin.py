from django.contrib import admin
from .models import (
    Earthquake,
    River,
    Rain,
    Fire,
    Pollution,
    Weather,
)
from bipad.admin import GeoModelAdmin

admin.site.register([Earthquake, River, Rain, Fire, Pollution, Weather], GeoModelAdmin)
