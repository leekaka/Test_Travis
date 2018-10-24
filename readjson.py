# !/usr/bin/env python

# coding=utf-8


import requests
import json

# 聚合数据天气预报 api
WEATHER_API = "http://t.weather.sojson.com/api/weather/city/{}"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
    "(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
}

def get_weather_info():
    city = "北京"
    city_code = get_city_code(city)
    weather_info = requests.get(WEATHER_API.format(city_code), headers=HEADERS).json()
    print(weather_info["data"]["forecast"][1])
   # print(weather_info["data"])
   # print(weather_info)



def get_city_code(city):
    with open("./_city.json",'r') as f:
        data = json.load(f)
        for dict in data:
            if dict["city_name"] == city:
                return (dict["city_code"])



if __name__ == "__main__":
    get_weather_info()


