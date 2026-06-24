import os

from groq import Groq

from dotenv import load_dotenv



load_dotenv()



client = Groq(

    api_key=os.getenv(
        "GROQ_API_KEY"
    )

)




def generate_response(question, articles):


    news_text = ""



    for article in articles:


        news_text += (

            "Title: "

            + article["title"]

            +

            "\nDescription: "

            +

            str(article["description"])

            +

            "\nSource: "

            +

            article["url"]

            +

            "\n\n"

        )





    prompt = f"""

You are a professional AI news assistant.


User question:

{question}


News articles:

{news_text}


Rules:

- Summarize only given articles.
- Do not invent information.
- Keep names and numbers correct.
- Select important updates only.
- Explain simply.
- Use bullet points.
- Always answer in English.
- Do not translate titles.
- Maximum 150 words.

"""



    response = client.chat.completions.create(


        model="llama-3.1-8b-instant",


        messages=[


            {

                "role":"system",

                "content":
                "You summarize news professionally."

            },


            {

                "role":"user",

                "content":prompt

            }

        ]

    )



    return response.choices[0].message.content