import tweepy
import time

auth = tweepy.OAuthHandler('YhoK35KEA3jmNg0MnrR6G3Zy2', 'aFbGyDzZmRBI6KT7Mwp8M9ad9VKbebIqRxqmacZxQs32zBYhK0')
auth.set_access_token('189273342-lZwPHy0cxYef6B1kOHNktssyWonqzNSNqmh2sNSl',
                      'K1IOgndun9wl8yTPzsTSQTNaKi4dMTTi6pQfdHebqYoHF')

api = tweepy.API(auth)
user = api.me()

print("Loading followers..")
followers = []
for follower in tweepy.Cursor(api.followers).items():
    followers.append(follower)

print(f"Found %s followers, finding friends.." % len(followers))
friends = []
for friend in tweepy.Cursor(api.friends).items():
    friends.append(friend)

# creating dictionaries based on id's is handy too

friend_dict = {}
for friend in friends:
    friend_dict[friend.id] = friend

follower_dict = {}
for follower in followers:
    follower_dict[follower.id] = follower

# now we find all your "non_friends" - people who don't follow you
# even though you follow them.

non_friends = [friend for friend in friends if friend.id not in follower_dict]

# double check, since this could be a rather traumatic operation.

print("Unfollowing %s non-following users.." % len(non_friends))
print("This will take approximately %s minutes." % (len(non_friends) / 60.0))

for nf in non_friends:
    print("Unfollowing " + str(nf.id).rjust(10))
    try:
        nf.unfollow()
    except tweepy.RateLimitError:
        print("  .. failed, sleeping for 5 seconds and then trying again.")
        time.sleep(5)
        nf.unfollow()
    print(" .. completed, sleeping for 1 second.")
    time.sleep(1)
