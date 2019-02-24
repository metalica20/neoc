from django.contrib import admin
from django.contrib.gis import forms
from .models import Alert


@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    point = forms.PointField(
        widget=forms.OSMWidget(
            default_lat=85,
            default_lon=85,
            default_zoom=30,
            attrs={'map_width': 8000, 'map_height': 500}
        )
    )
