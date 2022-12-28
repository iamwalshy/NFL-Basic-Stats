import streamlit as st
import tweepy

# Set up the Twitter API using your API keys
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Search for tweets with the hashtag #chatgpt
tweets = api.search_tweets(q="#chatgpt", lang="en", count=100)

st.title("#chatgpt Tweets")

# Display the tweets using Streamlit's dataframe function
st.dataframe(tweets)
