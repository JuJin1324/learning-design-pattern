# Created by Yoo Ju Jin(jujin@100fac.com)
# Created Date : 2020/08/03
# Copyright (C) 2020, Centum Factorial all rights reserved.
from __future__ import annotations

import pickle


class Url(object):
    short_url = ""
    full_url = ""

    @classmethod
    def shorten(cls, full_url: str) -> Url:
        """ Shortens full url. """

        # Create an instance of Url class
        instance = cls()
        instance.full_url = full_url
        instance.short_url = instance.__create_short_url()
        Url.__save_url_mapping(instance)
        return instance

    def __create_short_url(self) -> str:
        """ Creates short url, saves it and returns it. """
        last_short_url = Url.__load_last_short_url()
        short_url = self.__increment_string(last_short_url)
        Url.__save_last_short_url(short_url)
        return short_url

    def __increment_string(self, string) -> str:
        """ Increments string, that is:
            a -> b
            z -> aa
            az -> ba
            empty string -> a
        """
        if string == '':
            return 'a'

        last_char = string[-1]
        if last_char == 'z':
            # [:-1] -> 가장 마지막 값 빼고 모두
            return self.__increment_string(string[:-1]) + 'a'
        # chr(ASCII Code Number): ASCII Code Number to char
        # ex) chr(30) -> '0'
        # ord(char): char to ASCII Code Number
        # ex) ord('0') -> 30
        return string[:-1] + chr(ord(last_char) + 1)

    @staticmethod
    def __load_last_short_url() -> str:
        """ Returns last generated short url """
        try:
            return pickle.load(open("last_short.p", "rb"))
        except IOError:
            return ''

    @staticmethod
    def __save_last_short_url(url: str):
        """ Saves last generated short url. """
        pickle.dump(url, open("last_short.p", "wb"))

    @staticmethod
    def __load_url_mapping() -> dict:
        """ Returns short_url to Url instance mapping. """
        try:
            return pickle.load(open("short_to_url.p", "rb"))
        except IOError:
            return {}

    @staticmethod
    def __save_url_mapping(instance: Url):
        """ Saves short_url to Url instance mapping """
        short_to_url = Url.__load_url_mapping()
        short_to_url[instance.short_url] = instance
        pickle.dump(short_to_url, open("short_to_url.p", "wb"))

    @classmethod
    def get_by_short_url(cls, short_url: str) -> Url:
        """ Return Url instance, corresponding to short_url. """
        url_mapping = Url.__load_url_mapping()
        return url_mapping.get(short_url)
