import requests


def get_toponym_by_address(address, apikey):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": apikey,
        "geocode": address,
        "format": "json"
    }
    response = requests.get(geocoder_api_server, params=geocoder_params)
    if not response:
        raise RuntimeError("Geocoder request failed!")

    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    return toponym, tuple(float(x) for x in toponym_coodrinates.split(" "))


def get_org_closest_to(point, org, apikey, obj_type='biz', lang='ru_RU'):
    search_api_server = "https://search-maps.yandex.ru/v1/"
    search_params = {
        "apikey": apikey,
        "text": org,
        "lang": lang,
        "ll": ','.join(map(str, point)),
        "type": obj_type
    }

    response = requests.get(search_api_server, params=search_params)
    if not response:
        raise RuntimeError("Organization search failed!")

    json_response = response.json()

    organizations = json_response["features"]
    organizations = [(i["properties"]["CompanyMetaData"], tuple(i["geometry"]["coordinates"])) for i in organizations]
    return organizations


def get_toponym_spn(toponym):
    env_lower_corner = [float(x) for x in toponym['boundedBy']['Envelope']['lowerCorner'].split()]
    env_upper_corner = [float(x) for x in toponym['boundedBy']['Envelope']['upperCorner'].split()]
    return tuple(env_upper_corner[i] - env_lower_corner[i] for i in range(2))
