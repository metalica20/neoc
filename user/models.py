from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from federal.models import (
    Municipality,
    District,
    Province,
)

from organization.models import Organization


class Profile(models.Model):
    MUNICIPALITY = 'municipality'
    DISTRICT = 'district'
    PROVINCE = 'province'
    NATIONAL = 'national'

    REGIONS = (
        (MUNICIPALITY, 'Municipality'),
        (DISTRICT, 'District'),
        (PROVINCE, 'Province'),
        (NATIONAL, 'National'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(
        Organization,
        related_name='users',
        on_delete=models.SET_NULL,
        default=None, null=True, blank=True,
    )
    region = models.CharField(
        max_length=25,
        blank=True, null=True, default=None,
        choices=REGIONS
    )
    municipality = models.ForeignKey(
        Municipality,
        blank=True, null=True, default=None,
        related_name='users',
        verbose_name=_('Municipality'),
        on_delete=models.SET_NULL,
    )
    district = models.ForeignKey(
        District,
        blank=True, null=True, default=None,
        related_name='users',
        verbose_name=_('District'),
        on_delete=models.SET_NULL,
    )
    province = models.ForeignKey(
        Province,
        blank=True, null=True, default=None,
        related_name='users',
        verbose_name=_('Province'),
        on_delete=models.SET_NULL,
    )
    phone_number = models.CharField(
        max_length=17,
        default=None, null=True, blank=True,
    )
    opt_email_notification = models.BooleanField(default=False)
    opt_sms_notification = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
