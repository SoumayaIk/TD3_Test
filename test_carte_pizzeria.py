import unittest
from unittest.mock import MagicMock
from pizza import  Pizza
from carte_pizzeria import CartePizzeria
from carte_pizzeria_exception import CartePizzeriaException

class TestCartePizzeria(unittest.TestCase):
    
    def setUp(self):
        self.carte = CartePizzeria()

    def test_is_empty(self):
        self.assertTrue(self.carte.is_empty())
        self.carte.add_pizza(Pizza("Margherita", ["tomato sauce", "mozzarella", "basil"], 8.99))
        self.assertFalse(self.carte.is_empty())

    def test_nb_pizzas(self):
        self.assertEqual(self.carte.nb_pizzas(), 0)
        self.carte.add_pizza(Pizza("Margherita", ["tomato sauce", "mozzarella", "basil"], 8.99))
        self.assertEqual(self.carte.nb_pizzas(), 1)

    def test_add_pizza(self):
        pizza_mock = MagicMock()
        self.carte.add_pizza(pizza_mock)
        self.assertEqual(self.carte.menu, [pizza_mock])

    def test_remove_pizza_existing(self):
        pizza_margherita = Pizza("Margherita", ["tomato sauce", "mozzarella", "basil"], 8.99)
        self.carte.add_pizza(pizza_margherita)
        self.carte.remove_pizza("Margherita")
        self.assertEqual(self.carte.nb_pizzas(), 0)

    def test_remove_pizza_non_existing(self):
        with self.assertRaises(CartePizzeriaException):
            self.carte.remove_pizza("Hawaiian")

if __name__ == '__main__':
    unittest.main()
