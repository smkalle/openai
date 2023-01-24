import sys
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def answer(question):
	response = openai.Completion.create(
	  # model="text-davinci-003",
	  # model="davinci-instruct-beta",
	  model="text-curie-001",
	  prompt= question + "\\nA:",
	  temperature=0.2,
	  max_tokens=128,
	  top_p=1,
	  frequency_penalty=0,
	  presence_penalty=0
	)
	print(response["choices"][0].text)


openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.api_type = "azure"
# openai.api_base = "https://example-endpoint.openai.azure.com"
# openai.api_version = "2022-12-01"

print(openai.api_key)
print(sys.argv[1])
answer(sys.argv[1])
 

