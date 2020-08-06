from abc import ABC, abstractmethod

from addition.factory_method_pattern.pizza import Pizza, CheesePizza, PepperoniPizza, NormalPizza
from addition.factory_method_pattern.pizza_ingredient_factory import ChicagoPizzaIngredientFactory, \
    NYPizzaIngredientFactory


class PizzaStore(ABC):
    def order_pizza(self, type: str) -> Pizza:
        pizza = self.create_pizza(type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    @abstractmethod
    def create_pizza(self, type: str) -> Pizza:
        pass


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, type: str) -> Pizza:
        ingredient_factory = ChicagoPizzaIngredientFactory()

        if type == 'CHEESE':
            pizza = CheesePizza(ingredient_factory)
        elif type == 'PEPPERONI':
            pizza = PepperoniPizza(ingredient_factory)
        else:
            pizza = NormalPizza(ingredient_factory)

        return pizza


class NYPizzaStore(PizzaStore):
    def create_pizza(self, type: str):
        ingredient_factory = NYPizzaIngredientFactory()

        if type == 'CHEESE':
            pizza = CheesePizza(ingredient_factory)
        elif type == 'PEPPERONI':
            pizza = PepperoniPizza(ingredient_factory)
        else:
            pizza = NormalPizza(ingredient_factory)

        return pizza
