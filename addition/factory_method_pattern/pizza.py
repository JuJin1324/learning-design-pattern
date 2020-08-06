from abc import ABC, abstractmethod

from addition.factory_method_pattern.pizza_ingredient_factory import PizzaIngredientFactory


class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print(f'Bake: {self.name}')

    def cut(self):
        print(f'Cut: {self.name}')

    def box(self):
        print(f'Boxing: {self.name}')


class NormalPizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.factory = ingredient_factory
        self.name = 'Pizza'
        self.dough = 'None'
        self.sauce = 'None'

    def prepare(self):
        self.name = self.factory.get_name() + ' ' + self.name
        print(f'Prepare {self.name}')
        print(f'Dough: {self.dough}')
        print(f'Sauce: {self.sauce}')


class PepperoniPizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.factory = ingredient_factory
        self.name = 'Pepperoni Pizza'
        self.dough = 'None'
        self.sauce = 'None'

    def prepare(self):
        self.name = self.factory.get_name() + ' ' + self.name
        print(f'Prepare {self.name}')
        print(f'Dough: {self.dough}')
        print(f'Sauce: {self.sauce}')


class CheesePizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.factory = ingredient_factory
        self.name = 'Cheese Pizza'
        self.dough = 'None'
        self.sauce = 'None'

    def prepare(self):
        self.name = self.factory.get_name() + ' ' + self.name
        print(f'Prepare {self.name}')
        print(f'Dough: {self.dough}')
        print(f'Sauce: {self.sauce}')
