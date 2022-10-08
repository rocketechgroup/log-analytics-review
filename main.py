import json
import flask
import logging
import random
import string
import functions_framework

from flask import jsonify
from google.cloud import logging as gclogging

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
# attach gclogging to the root logger
client = gclogging.Client()
client.setup_logging()


def random_text():
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return x


@functions_framework.http
def log_tester(request: flask.Request):
    # root logger test with gclogging
    complex_log_details = {
        'source': "web",
        'details': {
            "id": "1",
            "type": "random_text",
            "name": random_text(),
            "image":
                {
                    "url": "img/01.png",
                    "width": 200,
                    "height": 200
                },
            "thumbnail":
                {
                    "url": "images/thumbnails/01.png",
                    "width": 32,
                    "height": 32
                }
        }
    }
    logging.getLogger().info(json.dumps(complex_log_details))
    return jsonify({'status': 'success'})


if __name__ == '__main__':
    log_tester('x')
