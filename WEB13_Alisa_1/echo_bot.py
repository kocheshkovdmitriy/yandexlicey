from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)


@app.route('/', methods=['POST'])
def main():

    req = request.json
    response = {
        'session': req['session'],
        'version': req['version'],
        'response': {
            'text': req['request']['original_utterance'],
            'tts': req['request']['original_utterance'],
            'end_session': False
        }
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run()