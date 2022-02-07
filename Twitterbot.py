"""
    Author: JaytechEnt

"""
from os import environ
from newsapi import NewsApiClient   
import datetime
import time
import tweepy

ACCESS_SECRET = environ['ACCESS_SECRET']
ACCESS_TOKEN = environ['ACCESS_TOKEN']
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET= environ['CONSUMER_KEY']

# Init
newsapi = NewsApiClient(api_key='3b968fb8dcb94113933ac4a01955e8a2')

                                         
                                         
                                         
                                     

                                      
                                                                   
                                     
                                                                                                today = datetime.date.today()
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
error_tweet = "Oops @Getinfotechent @token_surge something went wrong! Please get me back up and running soon."
 
def fetch():
    try:
        data = newsapi.get_everything(q='binance',from_param=today,
                                to=today,language='en',
                                sort_by='relevancy',
                                page_size=40)
        return data['articles']
    except:
        api.update_status(error_tweet)
    
def getList():
    articles = fetch()
    if len(articles) > 0:
        links = [article['url'] for article in articles]
    else:
        api.update_status(error_tweet)
    
    links = list(set(links)) 
    return links

def job():
    tweets = getList()
    for tweet in tweets:
        try: 
            api.update_status(tweet)
        except tweepy.TweepError as error:
            if error.api_code == 187:
                continue
        time.sleep(1800)

job()
