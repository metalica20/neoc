from modeltranslation.translator import register, TranslationOptions
from .models import Province, District, Municipality


@register([Province, District, Municipality])
class TranslationOptions(TranslationOptions):
    fields = ('title',)
