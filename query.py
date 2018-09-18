import sys

import base64
import json
import os
import requests

if __name__ == '__main__':

    arguments = sys.argv

    if len(arguments) < 3:
        print('Please specify an image and the server IP as arguments.')
        exit(1)

    img = os.path.expanduser(arguments[1])
    server_ip = arguments[2]

    with open(img, 'rb') as f:
        img_b64 = base64.b64encode(f.read()).decode()

    request = {'image': img_b64}

    response = requests.post('http://{}:5000/vision'.format(server_ip), json=request)

    assert response.status_code == 200

    response_dict = json.loads(response.content.decode('utf8'))

    print(json.dumps(response_dict, indent=4))
