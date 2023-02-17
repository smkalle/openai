import random

import openai
import tweepy
import wget
import sys
import time
import os


# OpenAI API endpoint for text generation
openai_endpoint = "https://api.openai.com/v1/engines/text-davinci-002/jobs"

# OpenAI API key
openai_api_key = "your_openai_api_key_here"

# Dall-E API endpoint for image generation
dalle_endpoint = "https://api.openai.com/v1/images/generations"

# Dall-E API key
dalle_api_key = "your_dalle_api_key_here"

# Zen Quotation prompt
prompt = "Generate Quotation Philosopher or Religious Guru or Stoic or Zen Monk as a Koan or Haiku"

# OpenAI API request to generate the quotation
def gen_output(input):

    seed = int(time.time())
    random.seed(seed)
    randnum = random.uniform(0.2, 1.2)
    print(seed)
    print(randnum)

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=input,
        temperature=randnum,
        max_tokens=256,
        top_p=1.0,
        frequency_penalty=0.2,
        presence_penalty=0.0,
    )
    print(response["choices"][0].text)
    return response["choices"][0].text


# check number of arguments if sys.argv[1] is not None:
if len(sys.argv) > 1:
    prompt = sys.argv[1]
zen_quotation = gen_output(prompt)

# Extract the generated quotation
print(zen_quotation)
# Dall-E API request to generate the image
response = openai.Image.create(
    prompt=zen_quotation,
    n=1,
    size="512x512"
)
image_url = response['data'][0]['url']
print(image_url)
filename = wget.download(image_url, out="/tmp/images")

print(filename)

# Twitter API endpoint for posting a tweet
twitter_endpoint = "https://api.twitter.com/1.1/statuses/update.json"

# Authentication keys and access tokens
consumer_key = os.getenv("TWITTER_API_KEY")
consumer_secret = os.getenv("TWITTER_API_KEY_SECRET")
access_token = os.getenv("TWITTER_API_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_API_ACCESS_TOKEN_SECRET")

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Initialize API client
api = tweepy.API(auth)

# tweet text and image file path
tweet_text = zen_quotation
image_path = filename

print("Tweeting :" + tweet_text)
print("Uploading :" + image_path)

# post tweet with image
try:
    api.update_status_with_media(tweet_text, image_path)
    print("Tweet posted with image successfully!")
except tweepy.TweepyException as error:
    print("Error while tweeting:", error)
