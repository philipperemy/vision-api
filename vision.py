from __future__ import print_function

import json
import os
import requests as r
from base64 import b64encode


def read_google_api_key():
    key = os.environ.get('GOOGLE_API_KEY')
    if key is None:
        raise Exception('The env variable GOOGLE_API_KEY is not defined. Export GOOGLE_API_KEY=<key>.')
    return key


def get_annotate_text(text, key, sentiment_analysis=False):
    url = 'https://language.googleapis.com/v1beta1/documents:annotateText?key={}'.format(key)
    data = dict()
    data['document'] = {
        'type': 'PLAIN_TEXT',
        'content': text,
    }
    data['encoding_type'] = 'UTF8'
    features = dict()
    features['extractEntities'] = True
    if sentiment_analysis:
        features['extractDocumentSentiment'] = True
    data['features'] = features
    print(data)
    return r.post(url, json=data).json()


def make_image_data_list(images, b64=True):
    """
    image_filenames is a list of filename strings
    Returns a list of dicts formatted as the Vision API
        needs them to be
    """

    def content(context):
        return {
            'image': {'content': context},
            'features': [
                {
                    'type': 'LABEL_DETECTION',
                    'maxResults': 10
                },
                {
                    'type': 'TEXT_DETECTION',
                    'maxResults': 10
                },
                {
                    'type': 'LOGO_DETECTION',
                    'maxResults': 10
                },
                {
                    'type': 'FACE_DETECTION',
                    'maxResults': 10
                },
                {
                    'type': 'LANDMARK_DETECTION',
                    'maxResults': 10
                },
                {
                    'type': 'SAFE_SEARCH_DETECTION',
                    'maxResults': 10
                }
            ]
        }

    img_requests = []
    if not b64:
        for img in images:
            with open(img, 'rb') as f:
                ctxt = b64encode(f.read()).decode()
                img_requests.append(content(ctxt))
    else:
        for img in images:
            img_requests.append(content(img))
    return img_requests


def make_image_data(images, b64=True):
    img_dict = make_image_data_list(images, b64)
    return json.dumps({"requests": img_dict}).encode()


def request_vision_api(image, b64=True):
    api_key = read_google_api_key()
    response = r.post('https://vision.googleapis.com/v1/images:annotate',
                      data=make_image_data([image], b64),
                      params={'key': api_key},
                      headers={'Content-Type': 'application/json'})
    return response


if __name__ == '__main__':
    import sys

    arguments = sys.argv

    if len(arguments) < 2:
        print('Please specify an image as argument.')
        exit(1)

    resp = request_vision_api(arguments[1], b64=False)
    dict_google_response = json.loads(resp.content)
    str_to_write = json.dumps(dict_google_response, indent=4)
    print(str_to_write)
