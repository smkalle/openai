import sys

import tweepy
# Twitter API endpoint for posting a tweet
twitter_endpoint = "https://api.twitter.com/1.1/statuses/update.json"

# Authentication keys and access tokens
consumer_key = "GX8bK14fVbFSX28xqtz4eI2Ho"
consumer_secret = "x1oswWgq9nGAbw16fZOhuJHvd69NVxuQbBfJ26SX5kgt7PxX7V"
access_token = "929010792-YUEWFZzGfjKHz0RvVm6xQAkbLagQu8LgdN0Hp3WF"
access_token_secret = "SSbh6JNohMPXRPUN4dqydS491MzO9rDTX8T8zHkDhkkRR"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Initialize API client
api = tweepy.API(auth)

# tweet text and image file path
tweet_text = sys.argv[1]
image_path = sys.argv[2]

print (tweet_text)
print (image_path)
# post tweet with image
try:
    # api.update_with_media(image_path, )
    # api.update_status_with_media(status=tweet_text, media=image_path)
    api.update_status_with_media(tweet_text, image_path)

    print("Tweet posted with image successfully!")
except tweepy.TweepyException as error:
    print("Error while tweeting:", error)
