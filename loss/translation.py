from modeltranslation.translator import register, TranslationOptions
from .models import LivestockType, InfrastructureType


@register([LivestockType, InfrastructureType])
class TranslationOptions(TranslationOptions):
    fields = ('title',)