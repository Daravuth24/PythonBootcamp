import requests


def patch_request():

    x = requests.patch('https://httpbin.org / patch', data ={'key':'value'})
    print(x.text)


patch_request()
