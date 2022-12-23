import smtplib
import ssl
import constants


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = constants.GMAIL_ACCOUNT
    password = constants.GMAIL_PASSWORD

    receiver = constants.TO_EMAIL_ADDRESS
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
