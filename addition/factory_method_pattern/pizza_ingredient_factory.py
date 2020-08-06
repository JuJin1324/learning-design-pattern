from abc import ABC, abstractmethod

from addition.factory_method_pattern.cheese import ChicagoCheese, NYCheese
from addition.factory_method_pattern.pepperoni import ChicagoPepperoni, NYPepperoni
from addition.factory_method_pattern.sauce import ChicagoSauce, NYSauce


class PizzaIngredientFactory(ABC):
    @abstractmethod
    def create_sauce(self):
        pass

    @abstractmethod
    def create_cheese(self):
        pass

    @abstractmethod
    def create_pepperoni(self):
        pass

    @abstractmethod
    def get_name(self):
        pass


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def get_name(self):
        return 'Chicago style'

    def create_pepperoni(self):
        return ChicagoPepperoni()

    def create_cheese(self):
        return ChicagoCheese()

    def create_sauce(self):
        return ChicagoSauce()


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def get_name(self):
        return 'NY style'

    def create_pepperoni(self):
        return NYPepperoni()

    def create_cheese(self):
        return NYCheese()

    def create_sauce(self):
        return NYSauce()
