from email import message
import requests
import os
from dotenv import load_dotenv
from send_email import send_email
import smtpd
import smtplib
import io
import ssl
load_dotenv()
topic = "tesla"
url = "https://newsapi.org/v2/everything?" \
    f"q={topic}&from=2023-04-29&sortBy=publishedAt&" \
    "apiKey=c4ac9731aede400ba1b9f83b01a2d57d&language=en"
api_key = os.environ.get("API")

request = requests.get(url)
content = request.json()


messages = ""

for article in content["articles"][:19]:
    messages = "Subject: New news" + "\n" + messages + (f"""{article["title"]}\n{article["description"]}\n{article["url"]}\n\n""")

messages = messages.encode("utf-8")
send_email(messages)
