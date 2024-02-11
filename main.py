from flask import Flask, jsonify, request
# import json
from json import JSONEncoder
from model.twit import Twit

twits = []

app = Flask(__name__)

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Twit):
            return {'body': obj.body, 'author': obj.author.username}
        else:
            return super().default(obj)

app.json_encoder = CustomJSONEncoder


@app.route('/ping', methods=['GET'])
def ping(): 
    return jsonify({'response': 'pong'})

@app.route('/twit', methods=['POST'])
def create_twit():
    # {"body": "Hello World", "author": "@Niko"} 

    twit_json = request.get_json()
    twit = Twit(twit_json['body'], twit_json['author'])
    twits.append(twit)
    return jsonify({'status': 'success'})


@app.route('/twit', methods=['GET'])
def read_twits():
    return jsonify({'twits': twits})


if __name__ == '__main__':
    app.run(debug=True)