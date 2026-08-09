import requests


KEY = "a8df30dbf720489e92d293b374f2exxx"

HOST = "jk3aat3894.re.qweatherapi.com"


def get_city_id(city_name):

    url = f"https://{HOST}/geo/v2/city/lookup"

    params = {
        "location": city_name,
        "key": KEY
    }

    res = requests.get(url, params=params)


    data = res.json()


    if data["code"] == "200":
        return data["location"][0]["id"]

    else:
        print(data)
        return None



def get_weather(city_id):

    url = f"https://{HOST}/v7/weather/now"


    params = {
        "location": city_id,
        "key": KEY
    }


    res = requests.get(url, params=params)


    data = res.json()


    if data["code"] == "200":

        now=data["now"]

        print("天气:",now["text"])
        print("温度:",now["temp"],"℃")
        print("湿度:",now["humidity"],"%")

    else:
        print(data)



city=input("请输入城市:")


city_id=get_city_id(city)


if city_id:
    get_weather(city_id)
