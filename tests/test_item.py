import pytest
import os
from src.item import Item


@pytest.fixture
def sample_item():
    return Item("SampleItem", 10.0, 5)


def test_item_creation(sample_item):
    assert sample_item.name == "SampleItem"
    assert sample_item.price == 10.0
    assert sample_item.quantity == 5


def test_item_name_length():
    with pytest.raises(ValueError, match="Длина наименования товара превышает 10 символов."):
        item = Item("TooLongItemName", 10.0, 5)


def test_calculate_total_price(sample_item):
    assert sample_item.calculate_total_price() == 50.0


def test_apply_discount(sample_item):
    Item.pay_rate = 0.8
    sample_item.apply_discount()
    assert sample_item.price == 8.0


def test_instantiate_from_csv(tmp_path):
    # Создаем временный каталог
    tmp_dir = tmp_path / "test_dir"
    tmp_dir.mkdir()

    # Создайте образец CSV-файла
    csv_content = "name,price,quantity\nItem1,10.0,5\nItem2,15.0,3"
    csv_path = tmp_dir / "items.csv"
    csv_path.write_text(csv_content)

    # Установить текущий каталог во временный каталог
    os.chdir(tmp_dir)

    # Протестируйте метод Instantiate_from_csv
    Item.instantiate_from_csv()

    # Проверьте, правильно ли загружены элементы
    assert len(Item.all) == 2
    assert Item.all[0].name == "Item1"
    assert Item.all[1].name == "Item2"


def test_string_to_number():
    assert Item.string_to_number("123") == 123
    assert Item.string_to_number("12.34") == 12.34


def test_add_item():
    item1 = Item("Item1", 10.0, 5)
    item2 = Item("Item2", 15.0, 3)

    assert Item.all == [item1, item2]


def test_get_all_items():
    item1 = Item("Item1", 10.0, 5)
    item2 = Item("Item2", 15.0, 3)

    assert Item.get_all_items() == [item1, item2]

def test_str_representation(sample_item):
    assert str(sample_item) == sample_item.name

def test_repr_representation(sample_item):
    expected_repr = f"Item('{sample_item.name}', {sample_item.price}, {sample_item.quantity})"
    assert repr(sample_item) == expected_repr

def test_add_quantity(sample_item):
    new_item = Item("New Item", 5.0, 2)
    result_item = sample_item.add_quantity(new_item)

    assert result_item.name == sample_item.name
    assert result_item.price == sample_item.price
    assert result_item.quantity == sample_item.quantity + new_item.quantity


def test_add_quantity_type_error(sample_item):
    with pytest.raises(TypeError, match="Неподдерживаемый тип для добавления"):
        sample_item.add_quantity("InvalidType")