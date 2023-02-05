import openai
import sys
import os



# OpenAI API request to generate the quotation
openai.api_key = os.getenv("OPENAI_API_KEY")


def gen_output(input):
    # print(input)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=input,
        temperature=0.5,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0,
        stop=["Human:", "AI:"],
    )
    # print(response["choices"][0].text)
    return (response["choices"][0].text)

print("Start your prompt:")
prompt=""
for line in sys.stdin:
    # print(line, end='')
    prompt += "\n Human: " + line + "\nAI:"
    print(prompt,end='')
    response = gen_output(prompt)
    prompt += response
    print(response,end='')
    print("\nHuman:")
