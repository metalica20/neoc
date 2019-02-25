from django.contrib import admin
from .models import (
    Earthquake,
    River,
    Rain
)


admin.site.register(Earthquake)

admin.site.register(River)

admin.site.register(Rain)
