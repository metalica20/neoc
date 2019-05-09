from django.core.mail import EmailMessage
import requests
from user.models import Profile
from .utils import alert_notification

SMS_API_URL = "http://202.70.80.2:8001/api/sms/"

params = {
    'from': 1133,
    'to': '',
    'token': 'IIPpW7uuEWvc62pQq6BR',
    'text': '',
}


def user_notifications(wards, obj, change):
    if not change:
        email = []
        phone_number = []
        for ward in wards:
            receivers = Profile.objects.filter(organization__ward=ward.id)
            for receiver in receivers:
                if receiver.user.email not in email:
                    email.append(receiver.user.email)
                    phone_number.append(receiver.phone_number)
        message = alert_notification(obj)
        params['text'] = obj.title + '\n' + obj.description
        receiver = email
        params['to'] = ','.join(phone_number)
        send_mail(obj.title, message, receiver)


def send_mail(subject, message, receiver):
    email = EmailMessage(subject, message, to=receiver)
    email.content_subtype = "html"
    requests.get(SMS_API_URL, params=params)
    email.send()
