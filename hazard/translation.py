from modeltranslation.translator import register, TranslationOptions
from .models import Hazard


@register(Hazard)
class HazardTranslationOptions(TranslationOptions):
    fields = ('title',)