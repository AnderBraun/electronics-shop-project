import pytest
from src.phone import Phone

# Тест на успешное создание объекта Phone
def test_phone_creation():
    phone = Phone('Samsung Galaxy S21', 1200, 3, 2)

    # Проверяем, что атрибуты установлены корректно
    assert phone.name == 'Samsung Galaxy S21'
    assert phone.price == 1200
    assert phone.quantity == 3
    assert phone.number_of_sim == 2

# Тест на успешное сложение двух объектов Phone
def test_phone_addition():
    phone1 = Phone('Samsung Galaxy S21', 1200, 3, 2)
    phone2 = Phone('iPhone 12', 1100, 2, 1)

    # Складываем два телефона и проверяем, что получилось правильное количество
    result = phone1 + phone2
    assert result == 5  # 3 (Samsung) + 2 (iPhone)

# Тест на успешное сложение Phone и Item
def test_phone_item_addition():
    phone = Phone('Samsung Galaxy S21', 1200, 3, 2)
    item = Item('USB Cable', 10, 5)

    # Складываем телефон и товар и проверяем, что получилось правильное количество
    result = phone + item
    assert result == 8  # 3 (Samsung) + 5 (USB Cable)

# Тест на попытку сложения с неподдерживаемым типом
def test_phone_invalid_addition():
    phone = Phone('Samsung Galaxy S21', 1200, 3, 2)

    # Пытаемся сложить телефон с неподдерживаемым типом и проверяем, что возникло исключение TypeError
    with pytest.raises(TypeError, match="Неподдерживаемый тип для добавления"):
        result = phone + 'invalid_type'