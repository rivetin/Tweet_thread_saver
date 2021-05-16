import tweepy
import os
from dotenv import load_dotenv
load_dotenv()
auth = tweepy.OAuthHandler(os.getenv("OAuthHandler"), os.getenv("OAuthHandler_2"))
auth.set_access_token(os.getenv("set_access_token"), os.getenv("set_access_token_2"))
api = tweepy.API(auth)
if api.verify_credentials() == False:
    print("Credentials are invalid.")
    exit()

f = open("tweets.txt", "w")
my_mentions = []
user_mentioned = []
k=0
user = api.me()
statuses = api.mentions_timeline()
for mention in statuses:
    my_mentions.append(mention.in_reply_to_status_id)
    user_mentioned.append(mention.user.screen_name)
for ids in my_mentions:
      
        if(ids!=None):
            getData=api.get_status(ids).text
            f.write(user_mentioned[k]+" : "+getData+"\n")
        k=k+1
