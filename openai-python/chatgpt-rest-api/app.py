# Flask app to serve the api
import openai
import os
import json
from flask import Flask, request, jsonify
app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route('/')
def index():    
        return '''
        <form action="/generate" method="post">
            <input type="text" name="prompt">
            <input type="submit" value="Generate">
        </form>
    '''


@app.route('/generate', methods=['POST'])
def api():
    prompt = request.form["prompt"]
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response["choices"][0]["text"]
    return jsonify({"message": message})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
