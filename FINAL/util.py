import wikipedia
from datetime import datetime
import requests
import pywhatkit as kit
#from google import search


opening_text = [
    "Cool, I'm on it sir.",
    "Okay sir, I'm working on it.",
    "Just a second sir.",
    "Okay sir, I'm on it.",
    "Getting it for you sir."
]

NEWS_API="1463eec76f4a4f8c98f3f3ecebbacffd"


def search_on_wikipedia(query):
    # wikipedia rest api
    # https://en.wikipedia.org/api/rest_v1/page/summary/{query}
    results = requests.get(f"https://en.wikipedia.org/api/rest_v1/page/summary/{query}").json()
    
    return results["extract"]
    

def play_on_youtube(video):
    kit.playonyt(video)


def search_on_google(query):
    #results = search(query, tld="co.in", num=10, stop=10, pause=2)
    kit.search(query)
    #return results

def get_latest_news():
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]





        