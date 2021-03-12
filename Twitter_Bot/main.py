import tweepy
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(50)


followers = limit_handler(tweepy.Cursor(api.followers).items())
following = limit_handler(tweepy.Cursor(api.friends).items())

followers2 = []
for follower in followers:
    followers2.append(follower)

following2 = []
for friend in following:
    following2.append(friend)

followers_dict = {}
for follower in followers2:
    followers_dict[follower.id] = follower

friend_dict = {}
for friend in following2:
    friend_dict[friend.id] = friend

non_followers = [friend for friend in following2 if friend.id not in followers_dict]


for nf in non_followers:
    if live_following == False:
        api.destroy_friendship(nf)
