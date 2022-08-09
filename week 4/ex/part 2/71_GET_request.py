import requests


def get_request():

    endpoint = "http://maps.googleapis.com/maps/api/geocode/json"
    location = "Phnom Penh"
    param = {'address': location}
    req = requests.get(url=endpoint, params=param)
    print(req.text)


get_request()
