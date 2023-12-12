#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def get_train_info():
    """
    Запросить данные о поезде.
    """
    destination = input("Название пункта назначения? ")
    train_number = input("Номер поезда? ")
    departure_time = input("Время отправления? ")

    # Создать словарь.
    return {
        'destination': destination,
        'train_number': train_number,
        'departure_time': departure_time,
    }


def display_trains(trains):
    """
    Отобразить информацию о поездах.
    """
    # Проверить, что список поездов не пуст.
    if trains:
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+'.format(
            '-' * 30,
            '-' * 10,
            '-' * 8
        )
        print(line)
        print(
            '| {:^30} | {:^10} | {:^8} |'.format(
                "Пункт назначения",
                "Номер поезда",
                "Время"
            )
        )
        print(line)

        # Вывести данные о всех поездах.
        for train in trains:
            print(
                '| {:<30} | {:^10} | {:^8} |'.format(
                    train.get('destination', ''),
                    train.get('train_number', ''),
                    train.get('departure_time', '')
                )
            )
        print(line)

    else:
        print("Список поездов пуст!", file=sys.stderr)


def main():
    """
    Главная функция программы.
    """
    # Список поездов.
    trains = []

    # Организовать бесконечный цикл запроса данных о поездах.
    while True:
        # Запросить данные о поезде.
        train = get_train_info()

        # Добавить словарь в список.
        trains.append(train)
        # Отсортировать список по времени отправления.
        trains.sort(key=lambda item: item.get('departure_time', ''))

        # Запросить команду из терминала.
        command = input("Введите название пункта назначения для отображения информации о поездах (введите 'exit' для выхода): ")

        if command == 'exit':
            break
        else:
            # Отобразить информацию о поездах, направляющихся в указанный пункт назначения.
            selected_trains = [train for train in trains if train['destination'] == command]
            display_trains(selected_trains)

if __name__ == '__main__':
    main()

