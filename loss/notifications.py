import os
from django.core.mail import EmailMessage
from .utils import (
    people_loss_notification,
    family_loss_notification,
    livestock_loss_notification,
    agriculture_loss_notification,
    infrastructure_loss_notification,
)
from .models import (
    People,
    Family,
    Livestock,
    Agriculture,
    Infrastructure,
)
import requests
from django.db.models import Sum
from user.models import Profile

SMS_API_URL = os.environ.get("SMS_API_URL")


def send_user_notification(incident, change):

    params = {
        'from': os.environ.get('SMS_FROM'),
        'to': '',
        'token': os.environ.get('SMS_API_TOKEN'),
        'text': '',
    }

    if not change:
        header = "{} Loss is added"

        people = People.objects.filter(loss=incident.loss)
        if people:
            status = people.values('status').order_by('status').annotate(total=Sum('count'))
            message, sms_message = people_loss_notification(people, status)
            subject = header.format("People")
            params['text'] = incident.title + sms_message
            receiver, params['to'] = get_email_receiver('People')
            send_mail(subject, message, receiver, params)

        family = Family.objects.filter(loss=incident.loss)
        if family:
            status = family.values('status').order_by('status').annotate(total=Sum('count'))
            message, sms_message = family_loss_notification(family, status)
            subject = header.format("Family")
            params['text'] = incident.title + sms_message
            receiver, params['to'] = get_email_receiver('People')
            send_mail(subject, message, receiver, params)

        livestock = Livestock.objects.filter(loss=incident.loss)
        if livestock:
            status = livestock.values('status').order_by('status').annotate(total=Sum('count'))
            message, sms_message = livestock_loss_notification(livestock, status)
            subject = header.format("Livestock")
            params['text'] = incident.title + sms_message
            receiver, params['to'] = get_email_receiver('Livestock')
            send_mail(subject, message, receiver, params)

        infrastructure = Infrastructure.objects.filter(loss=incident.loss)
        if infrastructure:
            status = infrastructure.values('status').order_by('status').annotate(total=Sum('count'))
            message, sms_message = infrastructure_loss_notification(infrastructure, status)
            subject = header.format("Infrastructure")
            params['text'] = incident.title + sms_message
            receiver, params['to'] = get_email_receiver('Infrastructure')
            send_mail(subject, message, receiver, params)

        agriculture = Agriculture.objects.filter(loss=incident.loss)
        if agriculture:
            status = agriculture.values('status', 'type__unit').order_by(
                'status').annotate(total=Sum('quantity'))
            message, sms_message = agriculture_loss_notification(agriculture, status)
            subject = header.format("Agriculture")
            params['text'] = incident.title + sms_message
            receiver, params['to'] = get_email_receiver('Agriculture')
            send_mail(subject, message, receiver, params)


def send_mail(subject, message, receiver, params):
    email = EmailMessage(subject, message, to=receiver)
    email.content_subtype = "html"
    requests.get(SMS_API_URL, params=params)
    email.send()


def get_email_receiver(department):
    sms_receivers = Profile.objects.filter(
        organization__responsible_for__title=department,
        opt_sms_notification=True,
        phone_number__isnull=False
    ).values_list('phone_number', flat=True)
    email_receivers = Profile.objects.filter(
        organization__responsible_for__title=department,
        opt_email_notification=True,
        user__email__isnull=False
    ).values_list('user__email', flat=True)
    return email_receivers, sms_receivers
