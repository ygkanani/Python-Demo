import tweepy
from credentials import bearer_token, consumer_key, consumer_secret, access_token, access_token_secret

client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)

usr = client.get_user(username="ygkanani")
public_tweets = client.get_users_tweets(usr.data.id)
for tweet in public_tweets:
    print(tweet)
