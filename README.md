# AI News Summarizer Chatbot 🤖📰

An AI-powered real-time news summarization chatbot that fetches latest news articles and generates concise summaries using Large Language Models.

## 🚀 Features

* Fetches real-time news using NewsAPI
* Generates AI-powered summaries using Llama-3.1-8B-Instant
* Fast response generation using Groq API's LPU inference engine
* Interactive chatbot interface built with Streamlit
* Custom prompt design for generating accurate and concise summaries

## 🛠️ Tech Stack

* Python
* Llama-3.1-8B-Instant (LLM)
* Groq API
* NewsAPI
* Streamlit
* Prompt Engineering

## 📌 Project Overview

Developed a real-time AI news summarization chatbot by integrating NewsAPI with the Llama-3.1-8B-Instant model. The application retrieves current news articles and uses Generative AI to automatically summarize content based on user queries.

The project demonstrates practical implementation of Large Language Models, API integration, prompt engineering, and AI-powered application development.

## ⚙️ How It Works

1. User enters a news-related query
2. NewsAPI fetches relevant articles
3. Extracted news content is processed
4. Llama-3.1-8B-Instant generates concise summaries
5. Streamlit displays the AI-generated response

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/Adithyamenon27/news_chatbot.git
```

Navigate to project folder:

```bash
cd news_chatbot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## 🔑 Environment Variables

Create a `.env` file in the project directory:

```env
GROQ_API_KEY=your_groq_api_key
NEWS_API_KEY=your_news_api_key
```

## 📂 Project Structure

```
news_chatbot/
│
├── app.py
├── chatbot.py
├── news_api.py
├── database.py
├── prompts.py
├── sentiment.py
├── test_news.py
├── requirements.txt
└── README.md
```

## 🎯 Skills Demonstrated

* Large Language Model (LLM) Integration
* Generative AI Application Development
* Prompt Engineering
* API Integration
* Streamlit Application Development
* AI-powered Text Summarization

