import requests


def put_request():

    x = requests.put("https://httpbin.org / put", data= {'key':'value'})
    print(x.text)


put_request()
