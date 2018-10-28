# !/usr/bin/env/ python

# coding=utf-8


import requests
import json
from common import *

# 聚合数据天气预报 api
WEATHER_API = "http://t.weather.sojson.com/api/weather/city/{}"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
    "(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
}

# 邮件内容
CONTENT_FROMAT = (    
    "\t亲爱的，早上好:\n\t"
    "\n\t今天是我们结婚的第{_loving_days}天：），\n"
    "\n\t让我来为你播报今日天气预报！祝你今天心情愉快！\n\n\t"
    "{_city}今天{_weather_high}，{_weather_low}，天气 {_weather_type}，"
    "{_weather_notice}."
)

def get_weather_info():
    city_code = get_city_code(CITY)
    weather_info = requests.get(WEATHER_API.format(city_code), headers=HEADERS).json()
    # print(weather_info["data"])
    return weather_info


def get_city_code(city):
    with open("./_city.json",'r') as f:
        data = json.load(f)
        for dict in data:
            if dict["city_name"] == city:
                return (dict["city_code"])

def get_date(info_data):
    """
    获取日期并且格式化
    """
    date = info_data["date"]
    week = info_data["data"]["forecast"][1]["date"][-3:]
    return "{}-{}-{}".format(date[:4],date[4:6],date[6:]),week


def get_content():
    w_info = get_weather_info()
    _date,_week = get_date(w_info)
    w_info = w_info["data"]["forecast"][0]

    return CONTENT_FROMAT.format(
        _week = _week,
        _date = _date,
        _loving_days = get_married_days(),
        _city = CITY,
     	_weather_high= w_info["high"],
     	_weather_low =    w_info["low"],
        _weather_type =   w_info["type"],
        _weather_notice = w_info["notice"],
    )


if __name__ == "__main__":
    print(get_content())

