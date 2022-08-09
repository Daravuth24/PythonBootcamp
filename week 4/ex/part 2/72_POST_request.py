import requests


def post_request():

    url = "https://httpbin.org"
    obj = {"key": "value"}

    x = requests.post(url, json=obj)
    print(x.text)


post_request()
