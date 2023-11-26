class Pizza:
    """Parent class for pizzas.

    Parameters:
    ----------
    name: str
        The name of the pizza.
    ingredients: list[str]
        The list of ingredients.
    size: str, default=\'L\', can only be \'L\' or \'XL\'
        The size of the pizza.
    """

    def __init__(self, name: str, ingredients: list[str], size: str = 'L'):
        self.name = name
        if size.upper() not in ['L', 'XL']:
            raise ValueError('The size of the pizza can either be L or XL')
        self.size = size.upper()
        self.ingredients = ingredients

    def __eq__(self, other) -> bool:
        """ Compares two pizzas, using names, sizes and ingredients. """
        if not isinstance(other, Pizza):
            return False

        return self.name == other.name and \
            self.size == other.size and    \
            self.ingredients == other.ingredients

    def dict(self) -> dict[str, str]:
        """ Outputs the recipe as a dictionary. """
        return {
            'name': self.name,
            'ingredients': ', '.join(self.ingredients),
            'size': self.size
        }


class Margherita(Pizza):
    """ Margherita🧀 pizza. """

    def __init__(self, size: str = 'L'):
        name = 'Margherita🧀'
        ingredients = [
            'tomato sauce',
            'mozzarella',
            'tomatoes'
        ]
        super().__init__(name, ingredients, size)


class Pepperoni(Pizza):
    """ Pepperoni🍕 pizza. """

    def __init__(self, size: str = 'L'):
        name = 'Pepperoni🍕'
        ingredients = [
            'tomato sauce',
            'mozzarella',
            'pepperoni'
        ]
        super().__init__(name, ingredients, size)


class Hawaiian(Pizza):
    """ Hawaiian🍍 pizza. """

    def __init__(self, size: str = 'L'):
        name = 'Hawaiian🍍'
        ingredients = [
            'tomato sauce',
            'mozzarella',
            'chicken',
            'pineapples'
        ]
        super().__init__(name, ingredients, size)
