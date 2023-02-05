import openai
import tweepy
import wget
import sys

# OpenAI API endpoint for text generation
openai_endpoint = "https://api.openai.com/v1/engines/text-davinci-002/jobs"

# OpenAI API key
openai_api_key = "your_openai_api_key_here"


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


stock_symbol = "'" + sys.argv[1] + "'"
count = sys.argv[2]
print(stock_symbol)
print(count)

# Get the last 100 tweets about a specific stock
# tweets = api.search(q=stock_symbol, count=sys.argv[2], lang='en', result_type='recent')
# Use a Tweepy cursor to get the last 100 tweets about a specific stock
tweets = tweepy.Cursor(api.search_tweets, q=stock_symbol, tweet_mode='extended').items(10)




# Initialize sentiment score
sentiment_score = 0
iter=0

# Loop through the tweets and get the sentiment of each
for tweet in tweets:
    print("Tweet:", tweet.full_text)
    # Use OpenAI to get the sentiment of the tweet

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="What is the sentiment of the tweet '" + tweet.full_text + "'?",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    iter+=1

    # Add the sentiment score to the total
    # print(response)
    # sentiment_score += response["choices"][0]["score"]
    print("Sentiment:", response["choices"][0]["text"])
       # Get the sentiment from the response
    sentiment = response["choices"][0]["text"]

    # Map the sentiment to a score
    #if sentiment contains "positive": add 1 to sentiment_score else subtract 1 from sentiment_score
    # varialbe contains string called positive
    if ("positive" in sentiment):
        sentiment_score += 1
    elif ("negative" in sentiment):
        sentiment_score -= 1
    elif ("angry" in sentiment):
        sentiment_score -= 1
    elif ("neutral" in sentiment):
        sentiment_score += 0

    print("Sentiment score:", sentiment_score)
# Calculate the average sentiment
average_sentiment = sentiment_score / iter

# Print the average sentiment
print("Average sentiment:", average_sentiment)

