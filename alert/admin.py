from django.contrib import (
    admin,
    messages,
)
from bipad.admin import GeoModelAdmin
from .models import Alert
from .utils import get_similar_alerts
from django.utils.safestring import mark_safe


@admin.register(Alert)
class AlertAdmin(GeoModelAdmin):
    search_fields = ('title', 'started_on', 'wards__title', 'wards__municipality__title',
                     'wards__municipality__district__title', 'hazard__title',)
    list_display = ('title', 'source', 'verified', 'public', 'started_on', 'expire_on', 'hazard',)
    exclude = ('wards',)

    def save_model(self, request, obj, form, change):
        super(AlertAdmin, self).save_model(request, obj, form, change)
        similar_alerts = get_similar_alerts(obj)
        for alert in similar_alerts:
            messages.add_message(request, messages.INFO, mark_safe(
                "Similar alert <a href='/admin/alert/alert/%d/change/'>%s</a> already exists"
                % (alert.id, alert.title)
            ))