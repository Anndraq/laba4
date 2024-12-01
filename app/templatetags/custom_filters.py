from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Получает элемент из словаря по ключу."""
    return dictionary.get(key, 0)  # Возвращает 0, если ключ не найден

@register.filter
def stars(value):
    """Возвращает строку из звездочек в зависимости от значения."""
    return '★' * value  # Возвращает звездочки, количество которых соответствует переданному значению

@register.filter
def multiply(value1, value2):
    """Умножает два значения."""
    return value1 * value2

@register.filter
def total_cost(cart_items):
    """Считает общую стоимость всех товаров в корзине."""
    total = sum(item.quantity * item.bike.price for item in cart_items)
    return total