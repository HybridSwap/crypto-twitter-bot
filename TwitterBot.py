"""
    Author: Dinah Johnson

"""

from newsapi import NewsApiClient
from api_key import my_api_key         
import datetime
import time
import tweepy
import schedule
from credentials import *  

todays_date = datetime.date.today()
news_api = NewsApiClient(api_key=my_api_key) 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def fetch():
    try:
        data = news_api.get_everything(q='cryptocurrency',from_param=todays_date,
                                to=todays_date,language='en',
                                sort_by='relevancy',
                                page_size=40)
        return data['articles']
    except:
        print("API error")
    
def getList():
    articles = fetch()
    links = []
    for article in articles:
        links.append(article['url'])
    return links

def job():
    tweets = getList()
    for tweet in tweets:
        api.update_status(tweet)
        time.sleep(1800)

job()
#schedule.every().day.at("08:00").do(job())