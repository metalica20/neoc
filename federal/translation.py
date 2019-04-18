from modeltranslation.translator import register, TranslationOptions
from .models import Province, District, Municipality, Ward


@register([Province, District, Municipality])
class TranslationOptions(TranslationOptions):
    fields = ('title',)
