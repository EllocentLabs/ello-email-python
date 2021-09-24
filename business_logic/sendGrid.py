import os

from django.template.loader import render_to_string
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

context = {
    "TWITTER_URL": "TWITTER_URL",
    "FB_URL": "FB_URL",
    "INSTA_URL": "INSTA_URL",
    "TELEGRAM_URL": "TELEGRAM_URL",
    "PRIVACY_URL": "PRIVACY_URL",
    "TERMS_CONDITION": "TERMS_CONDITION",
    "Fb_IMG": "Fb_IMG",
    "INSTA_IMG": "INSTA_IMG",
    "TWITTER_IMG": "TWITTER_IMG",
    "LOGO_IMG": "LOGO_IMG"
}


def forgot_pass_mail(email_id, url, name=""):
    context["url"] = url
    context["name"] = name
    message = Mail(
        from_email='itgeek.ellolabs@gmail.com',
        to_emails=email_id,
        subject='Forgot password',
        html_content=render_to_string('email/forgot_pass_mail.html', context))
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        sg.send(message)
    except Exception as e:
        print(str(e))


def signUp(email, name=""):
    context["name"] = name
    message = Mail(
        from_email='itgeek.ellolabs@gmail.com',
        to_emails=email,
        subject='Account created',
        html_content=render_to_string('email/signup.html', context))
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        sg.send(message)
    except Exception as e:
        print(str(e))


def otp_mail(email_id, otp, name=""):
    context["name"] = name
    context["otp"] = otp
    message = Mail(
        from_email='itgeek.ellolabs@gmail.com',
        to_emails=email_id,
        subject='Reset Password OTP',
        html_content=render_to_string('email/otp_mail.html', context))
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        sg.send(message)
    except Exception as e:
        print(str(e))


def verify_mail(email_id, url, name=""):
    context["url"] = url
    context["name"] = name
    message = Mail(
        from_email='itgeek.ellolabs@gmail.com',
        to_emails=email_id,
        subject='Email Address Verification',
        html_content=render_to_string('email/email_verification.html', context))
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        sg.send(message)
    except Exception as e:
        print(str(e))


def subscribe_mail(email_id, name=""):
    context["name"] = name
    message = Mail(
        from_email='itgeek.ellolabs@gmail.com',
        to_emails=email_id,
        subject='Subscribe',
        html_content=render_to_string('email/subscribe.html', context))
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        sg.send(message)
    except Exception as e:
        print(str(e))


def appointment_accept(email, name, nurse, url, time):
    context["name"] = name
    context["nurse"] = nurse
    context["url"] = url
    context["time"] = time
    message = Mail(
        from_email='itgeek.ellolabs@gmail.com',
        to_emails=email,  # user email
        subject='Appointment Status',
        html_content=render_to_string('email/appointment.html', context))
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        sg.send(message)
    except Exception as e:
        print(str(e))
