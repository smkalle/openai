import os
import openai
import sys

def chat(input):
	# prompt="Create a list of 8 questions for my interview with a science fiction author:\nCreate a list of 5 questions in Spanish\n",
	response = openai.Completion.create(
	# engine="deployment-name",
	model="text-davinci-003",
	  prompt= input,
	  temperature=0.2,
	  max_tokens=1000,
	  top_p=1.0,
	  frequency_penalty=0.2,
	  presence_penalty=0.0,
	)
	print(response["choices"][0].text)


openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.api_type = "azure"
# openai.api_base = "https://example-endpoint.openai.azure.com"
# openai.api_version = "2022-12-01"

print(openai.api_key)
print(sys.argv[1])

file1 = open(sys.argv[1], 'r')
count = 0
  
# Using for loop
for line in file1:
    print(line)
    chat(line)
    print("==========================")
# Closing files
file1.close()
# while line in sys.argv[1]:
    # chat(line)



# chat(sys.argv[1])
 

