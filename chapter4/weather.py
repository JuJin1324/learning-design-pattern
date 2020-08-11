# Created by Yoo Ju Jin(jujin@100fac.com) 
# Created Date : 2020/08/10
# Copyright (C) 2020, Centum Factorial all rights reserved.
import datetime
import json
import pickle
import urllib.parse

import requests


class WeatherProvider:
    def __init__(self):

        self.api_url = 'http://api.openweathermap.org/data/2.5/forecast?q={},{}&appid={}'

    def get_weather_data(self, city: str, country: str) -> str:
        api_key = 'Enter Your API Key'
        # urllib.parse.quote(str): encode str which is not encoded ASCII to ASCII to use url.
        # example: urllib.parse.quote('서울') => '%EC%84%9C%EC%9A%B8
        city = urllib.parse.quote(city)
        url = self.api_url.format(city, country, api_key)
        return requests.get(url).text


class Parser:
    @staticmethod
    def get_the_first_days_temp_list(parsed: json) -> list:
        start_date = None
        result = []

        for data in parsed['list']:
            date = datetime.datetime.strptime(data['dt_txt'], '%Y-%m-%d %H:%M:%S')
            start_date = start_date or date
            if start_date.day != date.day:
                return result
            result.append(data['main']['temp'])

    """
    weather_data is JSON format string
    sample)
    {
        "list": [
            {
                "main": {
                    "temp": 280.28,
                },
                "dt_txt": "2013-10-24 00:00:00",
            },
            {
                "main": {
                    "temp": 279.54,
                },
                "dt_txt": "2013-10-24 03:00:00"
            },
            {
                "main": {
                    "temp": 278.64,
                },
                "dt_txt": "2013-10-26 06:00:00"
            },
        ]
    }
    """

    def parse_weather_data(self, weather_data: str) -> list:
        parsed = json.loads(weather_data)
        return self.get_the_first_days_temp_list(parsed)


class Cache:
    def __init__(self, filename: str):
        self.filename = filename

    @staticmethod
    def get_datetime_after(hours=0) -> datetime:
        return datetime.datetime.utcnow() + datetime.timedelta(hours=hours)

    def save(self, obj):
        with open(self.filename, 'wb') as file:
            dct = {
                'obj': obj,
                'expired': self.get_datetime_after(hours=3)
            }
            pickle.dump(dct, file)

    def load(self):
        try:
            with open(self.filename, 'rb') as file:
                result = pickle.load(file)
                if result['expired'] > datetime.datetime.utcnow():
                    return result['obj']
        except IOError:
            pass


class Converter:
    @classmethod
    def from_kelvin_to_celcius(cls, kelvin: float) -> float:
        thermal_entropy = -273.15
        return kelvin + thermal_entropy


class Weather:
    def __init__(self, data: list):
        result = 0

        for r in data:
            result += r

        self.temperature = result / len(data)


class Facade:
    @classmethod
    def get_forecast(cls, city, country):
        cache_filename = 'myfile'
        cache = Cache(cache_filename)
        cache_result = cache.load()
        if cache_result:
            return cache_result
        else:
            weather_provider = WeatherProvider()
            weather_data = weather_provider.get_weather_data(city, country)

            parser = Parser()
            parsed_data = parser.parse_weather_data(weather_data)

            weather = Weather(parsed_data)
            converter = Converter()
            temperature_celcius = converter.from_kelvin_to_celcius(weather.temperature)

            cache.save(temperature_celcius)
            return temperature_celcius
