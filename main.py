import requests
import os
from dotenv import load_dotenv
load_dotenv()

url = os.environ.get("URL")
api_key = os.environ.get("API")

request = requests.get(url)
content = request.json()

for article in content["articles"]:
    print(article["title"])
    print(article["description"])