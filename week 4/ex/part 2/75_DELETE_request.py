import requests


def patch_request():

    x = requests.delete('https://httpbin.org / delete', data ={'key':'value'})
    print(x.text)


patch_request()
