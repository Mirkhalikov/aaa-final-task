from pizza import *
import unittest


class TestPizza(unittest.TestCase):
    def test_pizza_creation(self):
        pizza = Pizza('Margherita', ['cheese', 'tomato sauce'])
        self.assertEqual(pizza.name, 'Margherita')
        self.assertEqual(pizza.ingredients, ['cheese', 'tomato sauce'])
        self.assertEqual(pizza.size, 'L')
        pizza = Pizza('Margherita', ['cheese'], 'Xl')
        self.assertEqual(pizza.name, 'Margherita')
        self.assertEqual(pizza.ingredients, ['cheese'])
        self.assertEqual(pizza.size, 'XL')
        pizza = Pizza('Margherita', ['cheese'], 'l')
        self.assertEqual(pizza.name, 'Margherita')
        self.assertEqual(pizza.ingredients, ['cheese'])
        self.assertEqual(pizza.size, 'L')

    def test_pizza_equality(self):
        ingredients1 = ['cheese', 'tomato sauce']
        ingredients2 = ['cheese', 'pineapple']

        pizza1 = Pizza('Margherita', ingredients1)
        pizza2 = Pizza('Margherita', ingredients1)
        self.assertEqual(pizza1, pizza2)

        pizza1 = Pizza('Margherita', ingredients1, 'XL')
        self.assertNotEqual(pizza1, pizza2)

        pizza2 = Pizza('Pepperoni', ingredients1, 'XL')
        self.assertNotEqual(pizza1, pizza2)

        pizza2 = Pizza('Margherita', ingredients2, 'XL')
        self.assertNotEqual(pizza1, pizza2)

    def test_pizza_dictionary(self):
        pizza = Margherita('XL')

        expected_dict = {
            'name': 'Margherita🧀',
            'ingredients': 'tomato sauce, mozzarella, tomatoes',
            'size': 'XL'
        }

        self.assertEqual(pizza.dict(), expected_dict)


if __name__ == '__main__':
    # for unittest testing use $ python -m unittest -v tests.py

    # print tests:
    bake(Pepperoni())
    # Prints bake - {randint}c!, because template is None
    delivery(Pepperoni())
    # Prints 🛵Доставили за {randint}с!, because template is not None
    pickup(Pepperoni())
    # Prints 🏠Забрали за {randint}с!, because template is not None

