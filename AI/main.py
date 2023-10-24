import wikipedia
from datetime import datetime
from utils import opening_text
import requests
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from googlesearch import search


NEWS_API="1463eec76f4a4f8c98f3f3ecebbacffd"



def greet_user():
    """Greets the user according to the time"""
    
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        print(f"Good Morning sir.")
    elif (hour >= 12) and (hour < 16):
        print(f"Good afternoon sir.")
    elif (hour >= 16) and (hour < 19):
        print(f"Good Evening sir.")
    print(f"I am Jarvis. How may I assist you?")

def search_on_wikipedia(query):
    # wikipedia rest api
    # https://en.wikipedia.org/api/rest_v1/page/summary/{query}
    results = requests.get(f"https://en.wikipedia.org/api/rest_v1/page/summary/{query}").json()
    
    return results["extract"]
    



def play_on_youtube(video):
    kit.playonyt(video)


def search_on_google(query):
    results = search (query, tld="co.in", num=10, stop=10, pause=2)
    kit.search(query)
    return results

def get_latest_news():
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]

if __name__ == '__main__':
    greet_user()
    while True:
        query = str(input("Enter your query: ")).lower()

        if "wikipedia" in query:
            query = str(input("What do you want to search on wikipedia? ")).lower()
            print(opening_text[2])
            results = search_on_wikipedia(query)
            print(results)

        elif "youtube" in query:
            query = str(input("What do you want to search on youtube? ")).lower()
            print(opening_text[4])
            play_on_youtube(query)
        
        elif "google" in query:
            query = str(input("What do you want to search on google? ")).lower()
            print(opening_text[4])
            search_on_google(query)

        elif "news" in query:
            print(opening_text[4])
            news_headlines = get_latest_news()
            print(news_headlines)


        