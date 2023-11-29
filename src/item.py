import csv
import chardet
import os

class InstantiateCSVError(Exception):
    pass

class Item:
    all = []
    pay_rate = 1.0

    def __init__(self, name, price, quantity):
        self._name = name[:10]
        self.price = price
        self.quantity = quantity
        self.add_item()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            self._name = value[:10]
            raise ValueError("Длина наименования товара превышает 10 символов.")
        else:
            self._name = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price *= Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []  # Очистим список перед инициализацией
        current_dir = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(current_dir, 'items.csv')

        try:
            with open(filename, 'rb') as rawfile:
                result = chardet.detect(rawfile.read(10000))
                encoding = result['encoding']

            with open(filename, 'r', encoding=encoding) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    name = row['name']
                    price = float(row['price'])
                    quantity = int(row['quantity'])
                    item = cls(name, price, quantity)
        except FileNotFoundError as e:
            print(f"FileNotFoundError: {e}")
            raise e
        except csv.Error as e:
            print(f"CSV Error: {e}")
            raise InstantiateCSVError("Файл item.csv поврежден")

    @staticmethod
    def string_to_number(value):
        try:
            return int(value)
        except ValueError:
            return float(value)

    def add_item(self):
        Item.all.append(self)

    def get_all_items(self):
        return Item.all

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("Неподдерживаемый тип для добавления")

    def __radd__(self, other):
        if isinstance(other, int):
            return self.quantity + other
        else:
            raise TypeError("Неподдерживаемый тип для добавления")

    def add_quantity(self, other):
        if isinstance(other, Item):
            return Item(self.name, self.price, self.quantity + other.quantity)
        else:
            raise TypeError("Неподдерживаемый тип для добавления")
