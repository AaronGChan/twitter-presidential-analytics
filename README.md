# Twitter Sentiment Analysis
This project was to track sentiment related to President Biden and Donald Trump based on tweets. As Twitter is often reflective of society's views and feelings of a person, place, or thing, I thought it would be interesting to use Twitter to gauge public perception of the president and Trump.
- The tech stack I used was a python backend, with a google cloud function that is run every 8 days by a google cloud scheduler. I chose 8 days because the lookback for basic Twitter API for tweet searches is 8 days, and I wanted to not use the scheduler that much as the free tier only has 3 free jobs per month. (I know, I'm cheap XD) I then store all the data into bigquery tables with one table being all the tweets collected for each day of the last 8 days, and the other table is the subjectivity scores (positive, negative, neutral) counts for each day. I then pull the data into a streamlit app that I hosted on Heroku and containerize it with docker. 
- Link to the live app: https://twitter-presidential-analytics.herokuapp.com/
- Todo:
    - Add search capabilities to search for a particular subject. For example, let's say I want to see how people on Twitter feel about bitcoin, I could search that up and get various charts telling me the public sentiment.
    - Explore various sentiment analysis techniques, currently I'm using textblob to get polarity scores. I'm particularly interested in using LSTMs and gaining experience with deploying PyTorch models.
    - I'm currently only pulling in 15 tweets per day, I may expand that to 50 or 100, but I know that will start slowing down the backend, I will explore.
    
