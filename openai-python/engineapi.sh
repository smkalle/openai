# Description: Engine API
# 
curl https://api.openai.com/v1/engines \
  -H 'Authorization: Bearer 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'

curl https://api.openai.com/v1/engines/text-davinci-003 \

curl https://api.openai.com/v1/completions \
 -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer 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'
  -d '{
  "model": "text-davinci-003",
  "prompt": "Say this is a test",
  "max_tokens": 7,
  "temperature": 0,
  "top_p": 1,
  "n": 1,
  "stream": false,
  "logprobs": null,
  "stop": "\n"
}'

# Curl script to create edit with openai
curl https://api.openai.com/v1/edits \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer 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'
  -d '{
  "model": "text-davinci-003",
  "prompt": "Say this is a test",
  "max_tokens": 7,
  "temperature": 0.8,
  "top_p": 1,
  "n": 1,
  "stream": false,
  "logprobs": null,
  "stop": "\n"
}
'
