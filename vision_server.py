import json
from flask import Flask, jsonify
from flask import request

from vision import request_vision_api

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Vision API!"


@app.route("/vision", methods=['POST'])
def vision():
    img_b64 = request.json['image']
    resp = request_vision_api(img_b64, b64=True)
    dict_google_response = json.loads(resp.content)
    return jsonify(dict_google_response)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
