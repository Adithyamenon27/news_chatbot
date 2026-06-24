import os

from groq import Groq

from dotenv import load_dotenv



load_dotenv()



client = Groq(

    api_key=os.getenv(
        "GROQ_API_KEY"
    )

)




def analyze_sentiment(text):


    response = client.chat.completions.create(


        model="llama-3.1-8b-instant",


        messages=[


            {

            "role":"user",

            "content":f"""

Analyze this news summary.

Text:

{text}


Return:

Sentiment:
Reason:

"""

            }

        ]

    )



    return response.choices[0].message.content