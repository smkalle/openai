import os
import openai
import sys
import wget
input_text=sys.argv[1]
response = openai.Image.create(
  prompt=input_text,
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)
filename=wget.download(image_url,out="/tmp/images")
print(filename)

