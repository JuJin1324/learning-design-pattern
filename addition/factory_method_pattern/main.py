from addition.factory_method_pattern.pizza_store import ChicagoPizzaStore, NYPizzaStore

if __name__ == '__main__':
    chicago_store = ChicagoPizzaStore()
    ny_store = NYPizzaStore()

    ny_store.order_pizza('CHEESE')
    print("#"*50)
    chicago_store.order_pizza('PEPPERONI')
    print("#"*50)
    chicago_store.order_pizza('CHEESE')

