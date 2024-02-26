import requests
import math


def lonlat_distance(a, b):
    degree_to_meters_factor = 111 * 1000  # 111 километров в метрах
    a_lon, a_lat = a
    b_lon, b_lat = b

    # Берем среднюю по широте точку и считаем коэффициент для нее.
    radians_lattitude = math.radians((a_lat + b_lat) / 2.)
    lat_lon_factor = math.cos(radians_lattitude)

    # Вычисляем смещения в метрах по вертикали и горизонтали.
    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor

    # Вычисляем расстояние между точками.
    distance = math.sqrt(dx * dx + dy * dy)

    return distance


def dist(d) -> float:
    return math.sqrt((d - 3.6 * math.sqrt(525)) / 3.6)


geocoder_request_house = ("http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b"
                          f"&geocode={input('Адрес дома: ')}&format=json")

response_h = requests.get(geocoder_request_house)
if response_h:
    json_response_h = response_h.json()
    tower = [37.611776, 55.820952]
    home = list(map(float, json_response_h["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]["Point"]["pos"].split(' ')))
    print('~', round(dist(lonlat_distance(home, tower)), 2), 'метров')
else:
    print("Ошибка выполнения запроса")
