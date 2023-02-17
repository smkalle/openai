import sys
import os
import openai


def cmd(run_command, input):

	openai.api_key = os.getenv("OPENAI_API_KEY")

	text_file = open(input, "r")
	#read whole file to a string
	data = text_file.read()
	#close file
	text_file.close()

	openai.api_key = os.getenv("OPENAI_API_KEY")
	print(data)
	print('=' * 80)
	print(run_command)
	print('=' * 80)

	response = openai.Completion.create(
	  model="text-davinci-003",
      prompt=run_command + ":\n" + data,
	  temperature=0.2,
	  max_tokens=1024,
	  top_p=1,
	  frequency_penalty=0,
	  presence_penalty=0
	)
	print(response["choices"][0].text)

cmd(sys.argv[1],sys.argv[2])
