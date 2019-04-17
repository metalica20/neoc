from modeltranslation.translator import register, TranslationOptions
from .models import Province, District, Municipality, Ward


@register([Province, District, Municipality, Ward])
class TranslationOptions(TranslationOptions):
    fields = ('title',)