from functools import wraps
import click
import random


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
        """ Compares two pizzas, using names, sizes and ingredients 
        """
        return self.name == other.name and \
            self.size == other.size and    \
            self.ingredients == other.ingredients

    def dict(self) -> str:
        """ Outputs the recipe as a dictionary
        """
        return {
            'name': self.name,
            'ingredients': ', '.join(self.ingredients),
            'size': self.size
        }


class Margherita(Pizza):
    """ Margherita🧀 pizza.
    """

    def __init__(self, size: str = 'L'):
        name = 'Margherita🧀'
        ingredients = [
            'tomato sauce',
            'mozzarella',
            'tomatoes'
        ]
        super().__init__(name, ingredients, size)


class Pepperoni(Pizza):
    """ Pepperoni🍕 pizza.
    """

    def __init__(self, size: str = 'L'):
        name = 'Pepperoni🍕'
        ingredients = [
            'tomato sauce',
            'mozzarella',
            'pepperoni'
        ]
        super().__init__(name, ingredients, size)


class Hawaiian(Pizza):
    """ Hawaiian🍍 pizza.
    """

    def __init__(self, size: str = 'L'):
        name = 'Hawaiian🍍'
        ingredients = [
            'tomato sauce',
            'mozzarella',
            'chicken',
            'pineapples'
        ]
        super().__init__(name, ingredients, size)


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery',
              is_flag=True,
              default=False,
              help='Specify if pizza should be delivered')
@click.argument('pizza',
                type=click.Choice(['margherita', 'pepperoni', 'hawaiian']),
                default='margherita')
def order(pizza: str, delivery: bool) -> None:
    """Bakes and delivers pizza
    """
    s = f'👨‍🍳Приготовили за {random.randint(1, 10)}c!'
    if delivery:
        s += f'\n🛵Доставили за {random.randint(1, 10)}c!'
    click.echo(s)


@cli.command()
def menu() -> None:
    """Prints menu
    """
    for pizza in [Margherita(), Pepperoni(), Hawaiian()]:
        click.echo(
            f'- {pizza.name}:' + ', '.join(pizza.ingredients))


def log(template: str = None):
    """ If template is None - prints '<the name of the function> - <randint>c!1.
    Else usingincluding just randint in custom template.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if template is None:
                print('{} - {}c!'.format(
                    func.__name__, random.randint(1, 10)))
            else:
                print(template.format(random.randint(1, 10)))
            return result
        return wrapper
    return decorator


@log()
def bake(pizza: Pizza) -> None:
    """Bakes pizza"""
    pass


@log('🛵Доставили за {}с!')
def delivery(pizza: Pizza) -> None:
    """Delivers pizza"""
    pass


@log('🏠Забрали за {}с!')
def pickup(pizza: Pizza) -> None:
    """Pickups pizza"""
    pass


if __name__ == '__main__':
    cli()
