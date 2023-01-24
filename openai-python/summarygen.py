import sys
import os
import openai


def summarize(input):

	openai.api_key = os.getenv("OPENAI_API_KEY")

	text_file = open(input, "r")
	#read whole file to a string
	data = text_file.read()
	#close file
	text_file.close()

	openai.api_key = os.getenv("OPENAI_API_KEY")
	print(data)

	response = openai.Completion.create(
	  model="text-davinci-003",
	  prompt=data,
	  temperature=0.2,
	  max_tokens=256,
	  top_p=1,
	  frequency_penalty=0,
	  presence_penalty=0
	)
	print(response["choices"][0].text)

summarize(sys.argv[1])
