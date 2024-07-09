from flask import Flask, request, jsonify
from gpt4all import GPT4All

app = Flask(__name__)
gpt = GPT4All('gpt4all-model-path')

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data['messages'][0]['text']
    response = gpt.generate(message)
    return jsonify({'reply': response})

if __name__ == '__main__':
    app.run(port=5000)
