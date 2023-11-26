from pizza import Margherita, Pepperoni, Hawaiian
from functools import wraps
from typing import Optional
import click
import random


def log(template: Optional[str] = None):
    """ If template is None - prints '<the name of the function> - <randint>c!.
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
    s = [f'👨‍🍳Приготовили за {random.randint(1, 10)}c!']
    if delivery:
        s.append(f'🛵Доставили за {random.randint(1, 10)}c!')
    click.echo('\n'.join(s))


@cli.command()
def menu() -> None:
    """Prints menu. """
    for pizza in [Margherita(), Pepperoni(), Hawaiian()]:
        click.echo(
            f'- {pizza.name}:' + ', '.join(pizza.ingredients))


@cli.command()
@click.argument('pizza',
                type=click.Choice(['margherita', 'pepperoni', 'hawaiian']),
                default='margherita')
@log()
def bake(pizza: str) -> None:
    """Bakes pizza. """
    pass


@cli.command()
@click.argument('pizza',
                type=click.Choice(['margherita', 'pepperoni', 'hawaiian']),
                default='margherita')
@log('🛵Доставили за {}с!')
def delivery(pizza: str) -> None:
    """Delivers pizza. """
    pass


@cli.command()
@click.argument('pizza',
                type=click.Choice(['margherita', 'pepperoni', 'hawaiian']),
                default='margherita')
@log('🏠Забрали за {}с!')
def pickup(pizza: str) -> None:
    """Pickups pizza. """
    pass


if __name__ == '__main__':
    cli()
