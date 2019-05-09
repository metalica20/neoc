from modeltranslation.translator import register, TranslationOptions
from .models import LivestockType, InfrastructureType, DisabilityType, Country


@register([LivestockType, InfrastructureType, Country, DisabilityType])
class TranslationOptions(TranslationOptions):
    fields = ('title',)
