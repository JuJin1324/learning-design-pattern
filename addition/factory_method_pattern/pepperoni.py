from abc import ABC, abstractmethod


class Pepperoni(ABC):
    @abstractmethod
    def get_name(self):
        pass


class ChicagoPepperoni(Pepperoni):
    def get_name(self):
        return 'Chicago Pepperoni'


class NYPepperoni(Pepperoni):
    def get_name(self):
        return 'NY Pepperoni'
