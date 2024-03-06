from pizza import Pizza
from carte_pizzeria_exception import CartePizzeriaException

class CartePizzeria:
    
    def __init__(self):
        self.__pizzas = []

    def is_empty(self):
        return len(self.__pizzas)==0
    
    def nb_pizzas(self):
        return len(self.__pizzas)
    
    def add_pizza(self,pizza):
        self.__pizzas.append(pizza)

    def remove_pizza(self,name):
        for pizza in self.__pizzas:
            if pizza.get_pizza_name() == name:
                self.__pizzas.remove(pizza)
        raise CartePizzeriaException(f"La pizza {name} n existe pas dans la carte")
    


    