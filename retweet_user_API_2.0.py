import tweepy
from keys import *

# Use the API V2
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token, 
    access_token_secret=access_token_secret
)

########## REALTIME RETWEET USERS BY NAME ##########

class TweetListener(tweepy.StreamingClient):
    """Allows you to monitor a user and retweet all content in real time"""
    def on_tweet(self, tweet):
        print(tweet.text)
        client.retweet(tweet.id)
        print('Successfully retweeted!')   
    
stream = TweetListener(bearer_token=bearer_token) # Instantiating the class
 # Select one or more user to monitoring 
stream.add_rules(tweepy.StreamRule("from:username1 OR from:username2"))
stream.filter() # Now you can start monitoring with the rule sets
