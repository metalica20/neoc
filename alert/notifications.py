import os
from django.core.mail import EmailMessage
import requests
from user.models import Profile
from .utils import alert_notification

SMS_API_URL = os.environ.get("SMS_API_URL")

params = {
    'from': os.environ.get('SMS_FROM'),
    'to': '',
    'token': os.environ.get('SMS_API_TOKEN'),
    'text': '',
}


def send_user_notification(wards, obj, change):
    if not change:
        sms_receivers = Profile.objects.filter(
            organization__wards__in=wards,
            opt_sms_notification=True,
            phone_number__isnull=False
        ).values_list('phone_number', flat=True)
        params['to'] = sms_receivers
        params['text'] = obj.title + '\n' + obj.description
        requests.get(SMS_API_URL, params=params)
        email_receivers = Profile.objects.filter(
            organization__wards__in=wards,
            opt_email_notification=True,
            user__email__isnull=False
        ).values_list('user__email', flat=True)
        email_body = alert_notification(obj)
        send_mail(obj.title, email_body, email_receivers)


def send_mail(subject, message, receiver):
    email = EmailMessage(subject, message, to=receiver)
    email.content_subtype = "html"
    email.send()
