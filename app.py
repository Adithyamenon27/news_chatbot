import streamlit as st


from news_api import get_news

from chatbot import generate_response


from database import (

    create_table,

    save_message,

    get_messages

)





# ===============================
# PAGE SETTINGS
# ===============================


st.set_page_config(

    page_title="AI News Assistant",

    page_icon="📰",

    layout="wide"

)





# ===============================
# CSS
# ===============================


st.markdown(

"""

<style>


.stApp{

background:#f5f7fb;

}



.title{

font-size:42px;

font-weight:800;

color:#111827;

}



.subtitle{

font-size:18px;

color:#6b7280;

}



section[data-testid="stSidebar"]{

background:#111827;

}



section[data-testid="stSidebar"] *{

color:white;

}


</style>


""",

unsafe_allow_html=True

)







# ===============================
# DATABASE
# ===============================


create_table()







# ===============================
# SIDEBAR
# ===============================


with st.sidebar:



    st.title(
        "📰 AI News Bot"
    )



    st.write(

    """

    Features:


    ✅ Live news


    ✅ AI summary


    ✅ Chat memory


    ✅ Article links


    """

    )



    st.divider()



    if st.button(
        "🗑 Clear Chat"
    ):


        st.session_state.messages=[]

        st.rerun()







# ===============================
# HEADER
# ===============================


st.markdown(

"""

<div class="title">

📰 AI Powered News Chatbot

</div>


<div class="subtitle">

Ask about latest technology, sports, science and world news.

</div>


""",

unsafe_allow_html=True

)








# ===============================
# LOAD HISTORY
# ===============================



if "messages" not in st.session_state:



    st.session_state.messages=[]


    history=get_messages()



    for user,bot in history:



        st.session_state.messages.append(

        {

        "role":"user",

        "content":user

        }

        )



        st.session_state.messages.append(

        {

        "role":"assistant",

        "content":bot

        }

        )








# ===============================
# SHOW OLD CHAT
# ===============================



for message in st.session_state.messages:



    with st.chat_message(

        message["role"]

    ):


        st.write(

            message["content"]

        )









# ===============================
# USER INPUT
# ===============================


user_input = st.chat_input(

    "Example: latest AI news"

)








# ===============================
# PROCESS CHAT
# ===============================



if user_input:



    with st.chat_message(
        "user"
    ):


        st.write(user_input)



    st.session_state.messages.append(

    {

    "role":"user",

    "content":user_input

    }

    )






    # Fetch news


    with st.spinner(

        "🔎 Fetching news..."

    ):


        articles=get_news(

            user_input

        )







    # AI summary


    if articles:


        with st.spinner(

            "🤖 AI summarizing..."

        ):



            response=generate_response(

                user_input,

                articles

            )



    else:


        response=(

        "No news found for this topic."

        )







    # Display answer


    with st.chat_message(

        "assistant"

    ):



        st.write(response)



        st.divider()



        st.subheader(

            "🔗 News Sources"

        )






        for article in articles:



            st.markdown(

                f"### 📰 {article['title']}"

            )



            st.write(

                article["description"]

            )



            st.markdown(

                f"[🔗 Read Full Article]({article['url']})"

            )



            st.divider()







    # Save


    st.session_state.messages.append(

    {

    "role":"assistant",

    "content":response

    }

    )



    save_message(

        user_input,

        response

    )









# ===============================
# DOWNLOAD CHAT
# ===============================


chat_text=""


for message in st.session_state.messages:


    chat_text += (

    message["role"]

    +

    ":\n"

    +

    message["content"]

    +

    "\n\n"

    )





st.download_button(

    label="⬇ Download Chat History",

    data=chat_text,

    file_name="news_chat_history.txt"

)