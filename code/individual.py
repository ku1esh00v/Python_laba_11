#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def add_train(trains):
    """
    Функция для добавления информации о поезде в список trains.

    Parameters:
    trains (list): Список поездов.
    """
    destination = input('Название пункта назначения? ')
    number = input('Номер поезда? ')
    departure_time = input('Время отправления? ')

    train = {
        'destination': destination,
        'number': number,
        'departure_time': departure_time
    }

    trains.append(train)

    trains.sort(key=lambda item: item.get('departure_time', ''))


def list_trains(trains):
    """
    Функция для вывода списка всех поездов.

    Parameters:
    trains (list): Список поездов.
    """
    line = '+-{}-+{}-+{}-+'.format(
        '-' * 20,
        '-' * 15,
        '-' * 20
    )
    print(line)
    print(
        '| {:^20} | {:^15} | {:^20} |'.format(
            "Пункт назначения",
            "Номер поезда",
            "Время отправления"
        )
    )
    print(line)

    for idx, train in enumerate(trains, 1):
        print(
            '| {:<20} | {:^15} | {:^20} |'.format(
                train.get('destination', ''),
                train.get('number', ''),
                train.get('departure_time', '')
            )
        )
    print(line)


def select_trains(trains, command):
    """
    Функция для вывода информации о поездах в заданном пункте назначения.

    Parameters:
    trains (list): Список поездов.
    command (str): Команда в формате "select <пункт_назначения>".
    """
    parts = command.split(' ', maxsplit=1)
    destination = parts[1]

    selected_trains = [train for train in trains if train['destination'] == destination]

    if selected_trains:
        line = '+-{}-+{}-+{}-+'.format(
            '-' * 20,
            '-' * 15,
            '-' * 20
        )
        print(line)
        print(
            '| {:^20} | {:^15} | {:^20} |'.format(
                "Пункт назначения",
                "Номер поезда",
                "Время отправления"
            )
        )
        print(line)
        for train in selected_trains:
            print(
                '| {:<20} | {:^15} | {:^20} |'.format(
                    train.get('destination', ''),
                    train.get('number', ''),
                    train.get('departure_time', '')
                )
            )
        print(line)
    else:
        print(f'Поездов в пункт "{destination}" не найдено')


def show_help():
    """
    Функция для вывода списка доступных команд.
    """
    print('Список команд:\n')
    print('add - добавить информацию о поезде;')
    print('list - вывести список всех поездов;')
    print('select <пункт_назначения> - запросить информацию о поездах в заданном пункте назначения;')
    print('exit - завершить работу с программой.')


if __name__ == '__main__':
    trains = []

    while True:
        command = input('>>> ').lower()

        if command == 'exit':
            break
        elif command == 'add':
            add_train(trains)
        elif command == 'list':
            list_trains(trains)
        elif command.startswith('select '):
            select_trains(trains, command)
        elif command == 'help':
            show_help()
        else:
            print(f'Неизвестная команда "{command}"!', file=sys.stderr)
