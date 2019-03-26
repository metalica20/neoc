from django.contrib import admin
from .models import (
    Earthquake,
    River,
    Rain,
    Fire,
    Pollution,
)
from bipad.admin import GeoModelAdmin

admin.site.register([Earthquake, River, Rain, Fire, Pollution], GeoModelAdmin)
