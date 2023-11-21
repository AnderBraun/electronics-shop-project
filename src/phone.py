from src.item import Item

class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __add__(self, other):
        if isinstance(other, Item) or isinstance(other, Phone):
            # Вернуть только сумму количеств
            return self.quantity + other.quantity
        else:
            raise TypeError("Неподдерживаемый тип для добавления")

    def __repr__(self):
        return f"Смартфон('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
