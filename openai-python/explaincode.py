import os
import openai
import sys

def explain(input):

	openai.api_key = os.getenv("OPENAI_API_KEY")

	text_file = open(input, "r")
	#read whole file to a string
	data = text_file.read()
	#close file
	text_file.close()

	response = openai.Completion.create(
	  model="code-davinci-002",
	  prompt=data+"\"\"\"",
	  temperature=0.1,
	  max_tokens=128,
	  top_p=1,
	  frequency_penalty=0,
	  presence_penalty=0,
	  stop=["\"\"\""]
	)
	print(response["choices"][0].text)

openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.api_type = "azure"
# openai.api_base = "https://example-endpoint.openai.azure.com"
# openai.api_version = "2022-12-01"

# print(openai.api_key)
print("explain " + sys.argv[1])
explain(sys.argv[1]);
