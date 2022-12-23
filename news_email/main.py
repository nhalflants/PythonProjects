import requests
from send_email import send_email
import constants

url = "https://newsapi.org/v2/everything?" \
      "q=bitcoin&" \
      "language=en&" \
      f"apiKey={constants.NEWS_API_KEY}"

response = requests.get(url)
data = response.json()

content = "Subject: Today's News articles" + "\n"

for article in data["articles"]:
    if article["title"] is not None and article["description"] is not None:
        content = content + article["title"] + "\n" \
                  + article["description"] + "\n" \
                  + article["url"] + 2*"\n"

content = content.encode("utf-8")

send_email(content)
