# Google Vision API
Made easy!

## Get started in 2 min!

### Get the API key

- Browse here: [https://cloud.google.com/vision/](https://cloud.google.com/vision/)
- It should look like this: `AIzaSyD...4aA`. Mine has 39 characters.

### Run those commands to install the lib

```
git clone git@github.com:philipperemy/vision-api.git && cd vision-api
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

## Inference

### Command
```
export GOOGLE_API_KEY=AIzaSyD...4aA; python vision.py /tmp/cat.jpg
```

### Output
```
{
    "responses": [
        {
            "labelAnnotations": [
                {
                    "mid": "/m/01yrx",
                    "description": "cat",
                    "score": 0.99459696,
                    "topicality": 0.99459696
                },
                {
                    "mid": "/m/01l7qd",
                    "description": "whiskers",
                    "score": 0.9477582,
                    "topicality": 0.9477582
                },
                {
                    "mid": "/m/04rky",
                    "description": "mammal",
                    "score": 0.92298394,
                    "topicality": 0.92298394
                },
                {
                    "mid": "/m/07k6w8",
                    "description": "small to medium sized cats",
                    "score": 0.9217613,
                    "topicality": 0.9217613
                },
                {
                    "mid": "/m/0307l",
                    "description": "cat like mammal",
                    "score": 0.89394915,
                    "topicality": 0.89394915
                },
                {
                    "mid": "/m/035qhg",
                    "description": "fauna",
                    "score": 0.89245945,
                    "topicality": 0.89245945
                },
                {
                    "mid": "/m/012c9l",
                    "description": "domestic short haired cat",
                    "score": 0.777281,
                    "topicality": 0.777281
                },
                {
                    "mid": "/m/014sv8",
                    "description": "eye",
                    "score": 0.7664183,
                    "topicality": 0.7664183
                },
                {
                    "mid": "/m/05mqq3",
                    "description": "snout",
                    "score": 0.741837,
                    "topicality": 0.741837
                },
                {
                    "mid": "/m/0cnmr",
                    "description": "fur",
                    "score": 0.6560444,
                    "topicality": 0.6560444
                }
            ],
            "safeSearchAnnotation": {
                "adult": "VERY_UNLIKELY",
                "spoof": "UNLIKELY",
                "medical": "VERY_UNLIKELY",
                "violence": "VERY_UNLIKELY",
                "racy": "VERY_UNLIKELY"
            }
        }
    ]
}
```

## Server mode

Start the server:

```
export GOOGLE_API_KEY=AIzaSyD...4aA; python vision_server.py
```

In another tab you can query the server:

```
python query.py /tmp/cat.jpg 0.0.0.0
```

You can also host the server on Amazon AWS for example. You will have to change the IP to the IP Amazon gives you.

