from abc import ABC, abstractmethod


class Sauce(ABC):
    @abstractmethod
    def get_name(self):
        pass


class NYSauce(Sauce):
    def get_name(self):
        return 'NY Sauce'


class ChicagoSauce(Sauce):
    def get_name(self):
        return 'Chicago Sauce'
