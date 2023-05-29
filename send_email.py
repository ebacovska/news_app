from email import message
import smtpd
import smtplib
import ssl
import os
from dotenv import load_dotenv
load_dotenv()

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    usermane = os.environ.get("EMAIL")
    password = os.environ.get("PASSWORD_FOR_EMAIL")
    
    receiver = os.environ.get("EMAIL")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(usermane, password)
        server.sendmail(usermane, receiver, message)


