import pandas as pd
import streamlit as st
import plotly.express as px
from sqlalchemy import text
from sqlalchemy import create_engine

st.title("Presidential Rating based on Twitter Sentiment over Time")

db = create_engine('bigquery://', credentials_path="BIGQUERY_CREDENTIAL.json")


def get_scores():
    q = "select * from twittersentiment-339717.tweets.tweets_labeled"
    df = pd.read_sql(q, con = db)
    return df

df = get_scores()
df = df.sort_values(by=['tweet_date'])
df['pos_percentage'] = (df['pos']/15) * 100 


def plot_scores():
    fig = px.line(df, x="tweet_date", y="pos_percentage", color = 'query', title = "Percent of 15 Tweets that are Positive",
            labels = {'tweet_date': 'Date',
                      'pos_percentage': 'Percent of Positive Tweets (Out of 15)'})
    return fig
def plot_bars():
    fig_biden = px.bar(df[df['query'] == "biden"], x="tweet_date", y=["pos", "neg", "neu"], title="Biden Subjectivity Count by Date", labels = {'tweet_date': 'Date',
                      'value': 'Subjectivity Count', 'variable': ' Subjectivity'})
    fig_trump = px.bar(df[df['query'] == "trump"], x="tweet_date", y=["pos", "neg", "neu"], title="Trump Subjectivity Count by Date", labels = {'tweet_date': 'Date',
                      'value': 'Subjectivity Count', 'variable': ' Subjectivity'})
    return fig_biden, fig_trump

lineplot_fig = plot_scores()
st.plotly_chart(lineplot_fig)
biden_bar_fig, trump_bar_fig = plot_bars()
st.plotly_chart(biden_bar_fig)
st.plotly_chart(trump_bar_fig)
st.write(df)