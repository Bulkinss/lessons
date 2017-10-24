import requests
import json


def return_request(url):
    return json.loads(requests.get(url).text)
