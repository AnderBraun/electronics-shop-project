import pytest
from src.keyboard import Keyboard

# Тест на успешное создание объекта Keyboard
def test_keyboard_creation():
    kb = Keyboard('Dark Project KD87A', 9600, 5)

    # Проверяем, что атрибуты установлены корректно
    assert kb.name == 'Dark Project KD87A'
    assert kb.price == 9600
    assert kb.quantity == 5
    assert kb.language == 'EN'  # Проверяем, что язык установлен в значение по умолчанию

# Тест на успешное изменение языка
def test_keyboard_change_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)

    # Изменяем язык и проверяем, что значение изменилось
    kb.change_lang()
    assert kb.language == 'RU'

    # Изменяем язык еще раз и проверяем, что значение вернулось в исходное
    kb.change_lang()
    assert kb.language == 'EN'

# Тест на попытку изменения недопустимого языка
def test_keyboard_invalid_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)

    # Пытаемся установить недопустимый язык и проверяем, что возникло исключение ValueError
    with pytest.raises(ValueError, match="Допустимые значения языка: 'EN', 'RU'"):
        kb.language = 'CH'