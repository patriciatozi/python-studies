import tweepy
from settings import API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import settings

# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_KEY, 
    API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, 
    ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except Exception as e:
    print("Error during authentication")
    print(e)