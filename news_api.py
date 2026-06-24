import requests
import os
import re

from dotenv import load_dotenv


# Load .env file

load_dotenv()


NEWS_API_KEY = os.getenv(
    "NEWS_API_KEY"
)



# -----------------------------------
# Clean unwanted HTML/text
# -----------------------------------

def clean_text(text):

    if text:


        # remove html tags

        text = re.sub(
            "<.*?>",
            "",
            text
        )


        # remove extra spaces

        text = text.replace(
            "\n",
            " "
        )


        # limit length

        return text[:250]


    return "No description available"





# -----------------------------------
# Get News
# -----------------------------------

def get_news(topic):


    topic = topic.lower().strip()



    # General news keywords

    general_news = [

        "news",

        "latest news",

        "today news",

        "todays news",

        "current news",

        "today's news"

    ]




    # Categories

    categories = {


        "sports":"sports",

        "technology":"technology",

        "tech":"technology",

        "business":"business",

        "health":"health",

        "science":"science"

    }





    # -------------------------------
    # General headlines
    # -------------------------------


    if topic in general_news:



        url = (

        "https://newsapi.org/v2/top-headlines"

        )


        params = {


            "country":"us",

            "apiKey":NEWS_API_KEY,

            "pageSize":5


        }





    # -------------------------------
    # Category news
    # -------------------------------


    elif topic in categories:



        url = (

        "https://newsapi.org/v2/top-headlines"

        )


        params = {


            "category":categories[topic],

            "language":"en",

            "apiKey":NEWS_API_KEY,

            "pageSize":5


        }





    # -------------------------------
    # Search topic
    # -------------------------------


    else:



        url = (

        "https://newsapi.org/v2/everything"

        )


        params = {


            "q":topic,

            "language":"en",

            "sortBy":"publishedAt",

            "apiKey":NEWS_API_KEY,

            "pageSize":5


        }





    try:


        response = requests.get(

            url,

            params=params,

            timeout=10

        )



        if response.status_code != 200:


            return []




        data = response.json()



        articles = []




        for article in data.get(

            "articles",

            []

        ):



            title = clean_text(

                article.get("title")

            )


            description = clean_text(

                article.get("description")

            )


            link = article.get(

                "url",

                "#"

            )




            articles.append(

                {


                "title":title,


                "description":description,


                "url":link


                }

            )




        return articles





    except Exception as e:


        print(e)


        return []