import requests
import os
from dotenv import load_dotenv


load_dotenv()


NEWS_API_KEY = os.getenv("NEWS_API_KEY")


def get_news(topic):

    url = "https://newsapi.org/v2/everything"


    params = {

        "q": topic,

        "apiKey": NEWS_API_KEY,

        "language": "en",

        "sortBy": "publishedAt",

        "pageSize": 5
    }


    response = requests.get(
        url,
        params=params
    )


    if response.status_code != 200:

        return []


    data = response.json()


    articles = []


    for article in data.get("articles", []):


        title = article.get("title")

        description = article.get("description")

        url = article.get("url")


        if title and description:

            articles.append(
                {
                    "title": title,
                    "description": description,
                    "url": url
                }
            )


    return articles