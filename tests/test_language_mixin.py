import pytest
from src.language_mixin import LanguageMixin

# Тест на успешное создание объекта с использованием LanguageMixin
def test_language_mixin_creation():
    mixin_instance = LanguageMixin()

    # Проверяем, что язык установлен по умолчанию
    assert mixin_instance.language == 'EN'

# Тест на успешное изменение языка через setter
def test_language_mixin_setter():
    mixin_instance = LanguageMixin()

    # Изменяем язык и проверяем, что установлен корректный язык
    mixin_instance.language = 'RU'
    assert mixin_instance.language == 'RU'

# Тест на успешное получение языка через getter
def test_language_mixin_getter():
    mixin_instance = LanguageMixin()
    mixin_instance.language = 'RU'

    # Проверяем, что получен корректный язык
    assert mixin_instance.language == 'RU'

# Тест на успешное создание объекта с установкой языка при инициализации
def test_language_mixin_creation_with_language():
    mixin_instance = LanguageMixin(language='RU')

    # Проверяем, что язык установлен корректно при инициализации
    assert mixin_instance.language == 'RU'

# Тест на успешное изменение языка через метод change_language
def test_language_mixin_change_language_method():
    mixin_instance = LanguageMixin()

    # Изменяем язык через метод и проверяем, что установлен корректный язык
    mixin_instance.change_language('RU')
    assert mixin_instance.language == 'RU'