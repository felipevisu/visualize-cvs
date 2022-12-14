from django.conf import settings
from django.template.loader import render_to_string
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_cv_email(cv):
    context = {'cv': cv}

    message = Mail(
        from_email=settings.DEFAULT_FROM_EMAIL,
        to_emails=settings.DEFAULT_TO_EMAIL,
        subject='Novo currículo no site',
        html_content=render_to_string('jobs/cv.html', context)
    )
    try:
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        sg.send(message)
    except Exception as e:
        pass