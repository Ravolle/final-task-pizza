from __future__ import annotations
import random
import typing
import click


class Pizza:
    """Создаем базовый класс, от которого будем  наследовать"""

    def __init__(self, size: str, name: str, cook_time: int, recipe: dict):
        self.size = size
        self.name = name
        self.recipe = recipe
        self.cook_time = cook_time

    def cook(self) -> int:
        """Метод кук будет зависеть от размера пиццы"""
        if self.size == 'L':
            return self.cook_time + random.randrange(0, 5)
        else:
            return self.cook_time + random.randrange(0, 5) + 5

    def dict(self) -> dict:
        """Метод возвращает словарь"""
        return self.recipe

    def __eq__(self, other: object) -> bool:
        """Метод сравнивает две пиццы"""
        if not isinstance(other, Pizza):
            return NotImplemented
        if self.size == other.size and self.name == other.name:
            return True

        return False


class Margherita(Pizza):
    """Создаем класс Маргарита"""
    NAME = 'Margherita \U0001F9C0'
    RECIPE = {'Margherita \U0001F9C0': ['tomato sauce', 'mozzarella', 'tomatoes']}
    COOK_TIME = 10

    def __init__(self, size: str = 'L'):
        super().__init__(size, self.NAME, self.COOK_TIME, self.RECIPE)


class Pepperoni(Pizza):
    """Создаем класс Пепперони"""
    NAME = 'Pepperoni \U0001F355'
    RECIPE = {'Pepperoni \U0001F355': ['tomato sauce', 'mozzarella', 'pepperoni']}
    COOK_TIME = 12

    def __init__(self, size: str = 'L'):
        super().__init__(size, self.NAME, self.COOK_TIME, self.RECIPE)


class Hawaiian(Pizza):
    """Создаем класс Гавайская"""
    NAME = 'Hawaiian \U0001F34D'
    RECIPE = {'Hawaiian \U0001F34D': ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']}
    COOK_TIME = 15

    def __init__(self, size: str = 'L'):
        super().__init__(size, self.NAME, self.COOK_TIME, self.RECIPE)


@click.group()
def commanda():
    pass


def log(shablon: str):
    def printer_dec(f: typing.Callable):
        def printer(*args, **kwargs):
            return shablon.format(f(*args, **kwargs))

        return printer

    return printer_dec


@log('\U0001F6F5 Доставили за {} минут!')
def deliver() -> int:
    return random.randint(15, 30)


@log('\U0001F3E0 Заказ готов к выдаче!')
def pickup():
    pass


def process_order(name: str, delivery: str, size: str):
    """Создаем функцию заказ"""
    if name == 'margherita':
        margo = Margherita(size)
        cook_time = margo.cook()
    elif name == 'pepperoni':
        peppe = Pepperoni(size)
        cook_time = peppe.cook()
    else:
        hawa = Hawaiian(size)
        cook_time = hawa.cook()
    comp1 = f"\U0001F468\U0001F3FB\U0000200D\U0001F373 Приготовили за {cook_time} минут!"
    if delivery:
        comp2 = deliver()
    else:
        comp2 = pickup()
    return comp1 + '\n' + comp2

@commanda.command()
@click.option('--delivery/--no-delivery', default=False, help='How we will sent request?')
@click.option('--size', default='L', help='Pizza size?')
@click.argument('name')
def order(name: str, delivery: str, size: str):
    click.echo(process_order(name, delivery, size))


def pre_menu():
    """Создаем функцию меню"""
    margherita_rec = ', '.join(Margherita().dict()[Margherita.NAME])
    pepperoni_rec = ', '.join(Pepperoni().dict()[Pepperoni.NAME])
    hawaiian_rec = ', '.join(Hawaiian().dict()[Hawaiian.NAME])
    return f'- {Margherita.NAME}: {margherita_rec}\n- {Pepperoni.NAME}: {pepperoni_rec}\n- {Hawaiian.NAME}: {hawaiian_rec}'


@commanda.command()
def menu():
    click.echo(pre_menu())


if __name__ == '__main__':
    commanda()
