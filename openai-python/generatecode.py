import os
import openai
import sys

def generate(input, output):

	openai.api_key = os.getenv("OPENAI_API_KEY")

	text_file = open(output, "w")
	#read whole file to a string
	data = input #  text_file.read()
	#close file

	response = openai.Completion.create(
	  model="code-davinci-003",
	  prompt=data+"\"\"\"",
	  temperature=0.2,
	  max_tokens=1024,
	  top_p=1,
	  frequency_penalty=0,
	  presence_penalty=0,
	  stop=["\"\"\""]
	)
	print(response["choices"][0].text)
	text_file.write(response["choices"][0].text)
	text_file.close()

openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.api_type = "azure"
# openai.api_base = "https://example-endpoint.openai.azure.com"
# openai.api_version = "2022-12-01"

# print(openai.api_key)
# print("convert C++ to java " + sys.argv[1])
generate(sys.argv[1], sys.argv[2])
