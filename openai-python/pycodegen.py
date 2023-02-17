import openai
import sys
import os

# Check if two command line arguments are provided
if len(sys.argv) != 3:
    print("Error: Invalid number of arguments.")
    print("Usage: python code_generator.py <description> <output_file>")
    sys.exit(1)

# Store the description and output file name
description = sys.argv[1]
print(description)
output_file = sys.argv[2]
print(output_file)

# Use the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Generate code using the OpenAI "Davinci" model

response = openai.Completion.create(
  model="code-davinci-002",
  prompt=description+"\"\"\"",
  temperature=0.2,
  max_tokens=1024,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=["\"\"\""]
)
print(response["choices"][0].text)

# Store the generated code in a file
with open(output_file, "w") as f:
    f.write(response["choices"][0]["text"])

print(f"Generated code is written to {output_file}")
f.close()

