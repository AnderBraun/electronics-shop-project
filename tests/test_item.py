import os
import pytest
from src.item import Item, InstantiateCSVError

# Тест на успешное создание объектов Item из CSV
def test_instantiate_from_csv_success(tmpdir):
    # Создаем временный файл CSV с корректными данными
    csv_data = "name,price,quantity\nitem1,10.0,5\nitem2,20.0,3"
    csv_file = tmpdir.join("items.csv")
    csv_file.write(csv_data)

    # Переходим во временную директорию, чтобы файл items.csv был виден
    os.chdir(tmpdir)

    # Вызываем метод instantiate_from_csv и проверяем, что объекты Item созданы
    Item.instantiate_from_csv()
    items = Item.get_all_items()
    assert len(items) == 2

# Тест на обработку ошибки отсутствия файла items.csv
def test_instantiate_from_csv_file_not_found(tmpdir):
    # Переходим во временную директорию, чтобы файл items.csv не был виден
    os.chdir(tmpdir)

    # Вызываем метод instantiate_from_csv и проверяем, что возникло исключение FileNotFoundError
    with pytest.raises(FileNotFoundError, match="Отсутствует файл item.csv"):
        Item.instantiate_from_csv()

# Тест на обработку ошибки поврежденного файла items.csv
def test_instantiate_from_csv_corrupted_file(tmpdir):
    # Создаем временный файл CSV с некорректными данными (без колонки quantity)
    csv_data = "name,price\nitem1,10.0\nitem2,20.0"
    csv_file = tmpdir.join("items.csv")
    csv_file.write(csv_data)

    # Переходим во временную директорию, чтобы файл items.csv был виден
    os.chdir(tmpdir)

    # Вызываем метод instantiate_from_csv и проверяем, что возникло исключение InstantiateCSVError
    with pytest.raises(InstantiateCSVError, match="Файл item.csv поврежден"):
        Item.instantiate_from_csv()