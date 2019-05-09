from modeltranslation.translator import register, TranslationOptions
from .models import IncidentSource


@register(IncidentSource)
class IncidentSourceTranslationOptions(TranslationOptions):
    fields = ('display_name',)
