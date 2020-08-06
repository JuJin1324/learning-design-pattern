from abc import ABC, abstractmethod


class Cheese(ABC):
    @abstractmethod
    def get_name(self):
        pass


class NYCheese(Cheese):
    def get_name(self):
        return 'NY Cheese'


class ChicagoCheese(Cheese):
    def get_name(self):
        return 'Chicago Cheese'
