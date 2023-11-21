from src.language_mixin import LanguageMixin
from src.item import Item  # Импортируем класс Item

class Keyboard(LanguageMixin, Item):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self._language = 'EN'  # Установить язык по умолчанию

    def change_lang(self):
        self._language = 'RU' if self._language == 'EN' else 'EN'
