from modeltranslation.translator import register, TranslationOptions
from .models import LivestockType, InfrastructureType, DisabilityType


@register([LivestockType, InfrastructureType, DisabilityType])
class TranslationOptions(TranslationOptions):
    fields = ('title',)