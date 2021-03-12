import tweepy
import time

auth = tweepy.OAuthHandler('YhoK35KEA3jmNg0MnrR6G3Zy2', 'aFbGyDzZmRBI6KT7Mwp8M9ad9VKbebIqRxqmacZxQs32zBYhK0')
auth.set_access_token('189273342-lZwPHy0cxYef6B1kOHNktssyWonqzNSNqmh2sNSl',
                      'K1IOgndun9wl8yTPzsTSQTNaKi4dMTTi6pQfdHebqYoHF')

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