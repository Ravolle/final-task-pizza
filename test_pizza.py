import pytest

from pizza import process_order
from pizza import pre_menu
from pizza import Margherita
from pizza import Pepperoni
from pizza import Hawaiian


def test_process_order_pickup():
    """Тестируем функцию ордер на самовывоз"""
    has_prefix = '👨🏻‍🍳 Приготовили за '
    has_postfix = ' минут!\n🏠 Заказ готов к выдаче!'
    minutes_min = 9
    minutes_max = 26
    result = process_order('pepperoni', '', '')
    assert result.startswith(has_prefix)
    assert result.endswith(has_postfix)
    assert minutes_min < int(result[19:22]) < minutes_max


def test_process_order_delivery():
    """Тестируем функцию ордер на доставку"""
    has_prefix = '👨🏻‍🍳 Приготовили за '
    has_postfix = ' минут!'
    between = 'минут!\n🛵 Доставили за'
    minutes_min = 9
    minutes_max = 26
    delivery_minutes_min = 14
    delivery_minutes_max = 31
    result = process_order('pepperoni', 'delivery', '')
    assert between in result
    assert result.startswith(has_prefix)
    assert result.endswith(has_postfix)
    assert minutes_min < int(result[20:22]) < minutes_max
    assert delivery_minutes_min < int(result[45:47]) < delivery_minutes_max


def test_pre_menu():
    """Тестируем функцию меню"""
    expected = '- Margherita 🧀: tomato sauce, mozzarella, tomatoes\n- Pepperoni 🍕: tomato sauce, mozzarella, pepperoni\n- Hawaiian 🍍: tomato sauce, mozzarella, chicken, pineapples'
    assert pre_menu() == expected


def test_pizza_eq():
    """Тестируем метод равенства пицц"""
    peppe_1 = Pepperoni('L')
    peppe_2 = Pepperoni('L')
    margo_1 = Margherita('XL')
    margo_2 = Margherita('XL')
    hawa_1 = Hawaiian('L')
    hawa_2 = Hawaiian('XL')
    assert peppe_1.__eq__(peppe_2)
    assert margo_1.__eq__(margo_2)
    assert not hawa_1.__eq__(hawa_2)


def test_pizza_eq_error():
    """Тестируем метод равенства пицц (на исключение)"""
    peppe_1 = Pepperoni('L')
    pizza_name = 'Pepperoni'
    assert peppe_1.__eq__(pizza_name) == NotImplemented
