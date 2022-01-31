# Twitter Sentiment Analysis
This project was to track sentiment related to President Biden and Donald Trump based on tweets. As twitter is often reflective of socities views and feelings of a person, place, or thing, I thought i would be interesting to use twitter to gauge public perception of the president and Trump.
- The tech stack I used was a python backend, with google cloud function that is run every 8 days by google cloud scheduler. I chose 8 days because the lookback for basic twitter api for tweet searches is 8 days, and I wanted to not use the scheduler that much as the free tier only has 3 free jobs per month. (I know, I'm cheap XD) I then store all the data in to bigquery tables with one table being all the tweets collected for each day of the last 8 days, and the other table being the subjectivity scores (positive, negative, neutral) counts for each day. I then pull the data into a streamlit app that I hosted on Heroku and containerized with docker. 
- Link to the live app: https://twitter-presidental-analytics.herokuapp.com/
- Todo:
    - Add search capabilities to search for a particular subject. For example, lets say I want to see how people on twitter feel about bitcoin, I could search that up and get various charts telling me the public sentiment.
    - Explore various sentiment analysis techniques, currently I'm using textblob to get polarity scores. I'm particuarly interested in using LSTMs and gaining experience with deploying PyTorch models.
    - Currently only pulling in 15 tweets per day, I may expand that to 50 or 100, but I know that will start slowing down the backend, I will explore.
    
