import openai
import tweepy
import wget

# OpenAI API endpoint for text generation
openai_endpoint = "https://api.openai.com/v1/engines/text-davinci-002/jobs"

# OpenAI API key
openai_api_key = "your_openai_api_key_here"

# Dall-E API endpoint for image generation
dalle_endpoint = "https://api.openai.com/v1/images/generations"

# Dall-E API key
dalle_api_key = "your_dalle_api_key_here"

# Zen Quotation prompt
prompt = "Generate  Zen Quotation about Morning Light Energy by any Ancient Philosopher or Religious Guru or Stoic as a Koan or Haiku"


# OpenAI API request to generate the quotation
def gen_output(input):
    print(input)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=input,
        temperature=0.8,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.2,
        presence_penalty=0.0,
    )
    print(response["choices"][0].text)
    return (response["choices"][0].text)


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
