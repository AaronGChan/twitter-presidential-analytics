import tweepy
import datetime
from config import consumer_key, consumer_secret, access_token, access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def get_tweets(query, number_of_tweets=10, date=None):
    tweets = []
    dates = []
    tweet_ids = []
    if date is None:
        date = str(datetime.date.today())
    for tweet in tweepy.Cursor(api.search_tweets,
                                q=query,
                                lang="en",
                                count = number_of_tweets,
                                until=date,
                                tweet_mode='extended').items(number_of_tweets):
        dates.append(tweet._json['created_at'])
        tweets.append(tweet._json['full_text'])
        tweet_ids.append(tweet._json['id'])
    return tweets, dates, tweet_ids
