"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
person  = [
    {"name": "Bob", "age": 28, "job": "Baker"},
    {"name": "Tom", "age": 30, "job": "Driver"},
    {"name": "John", "age": 20, "job": "Bartender"},
    {"name": "Mark", "age": 40, "job": "Teacher"},
]

with open(file="users.csv", mode='w', encoding="utf-8", newline="") as table:
    fields = ["name", "age", "job"]
    writer = csv.DictWriter(table, fields, delimiter=",")
    writer.writeheader()
    for user in person:
        writer.writerow(user)

if __name__ == "__main__":
    main()
