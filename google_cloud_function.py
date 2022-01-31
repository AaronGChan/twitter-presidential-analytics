from tweets import get_tweets
from util import cleanUpTweet, getTextSubjectivity, getTextAnalysis, getTextPolarity
import datetime
import pandas as pd
from sqlalchemy import text
from sqlalchemy import create_engine
import numpy as np
def tweets_to_database(topic, date):
    tweets, dts, tweet_ids = get_tweets(topic, 15, date)
    tweets = list(map(cleanUpTweet, tweets))
    db = create_engine('bigquery://', credentials_path="BIGQUERY_CREDENTIAL.json")
    headers = ['twitter_id', 'tweet_date', 'tweet', 'query']
    queries = [topic]*len(tweets)
    dates = [date] * len(tweets)
    lists = [tweet_ids, dates, tweets, queries]
    df = pd.DataFrame(lists).transpose()
    df.columns = headers
    df.to_sql('twittersentiment-339717.tweets.tweets', db, if_exists='append', index=False)
    df = pd.DataFrame(data=[tweet for tweet in tweets], columns=['Tweet'])
    df['Tweet'] = df['Tweet'].apply(cleanUpTweet)
    df['Date'] = date
    df['Subjectivity'] = df['Tweet'].apply(getTextSubjectivity)
    df['Polarity'] = df['Tweet'].apply(getTextPolarity)
    df = df.drop(df[df['Tweet'] == ''].index)
    df['Score'] = df['Polarity'].apply(getTextAnalysis)
    labels = df.groupby('Score').count().index.values
    values = df.groupby('Score').size().values
    if "Negative" not in labels:
        values = np.insert(values, 0, 0)
    if "Neutral" not in labels:
        values = np.insert(values, 1, 0)
    if "Positive" not in labels:
        values = np.append(values, 0)
    neg = int(values[0])
    neu = int(values[1])
    pos = int(values[2])
    lists = [[date], [pos], [neg], [neu], [topic]]
    df_labeled = pd.DataFrame(lists).transpose()
    headers = ['tweet_date', 'pos', 'neg', 'neu', 'query']
    df_labeled.columns = headers
    df_labeled.to_sql('twittersentiment-339717.tweets.tweets_labeled', db, if_exists='append', index=False)
    return True

def etl_tweets(request):
    dates = []
    for i in range(0, 8):
        dates.append(str(datetime.date.today() - datetime.timedelta(days=i)))
    dates = dates[::-1]
    for date in dates:
        tweets_to_database("biden", date)
        tweets_to_database("trump", date)