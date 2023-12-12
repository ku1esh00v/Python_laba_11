#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_input():
    """
    Запросить ввод с клавиатуры и вернуть полученную строку.
    """
    return input("Введите значение: ")


def test_input(value):
    """
    Проверить, можно ли значение преобразовать к целому числу.
    Если можно, вернуть True, иначе False.
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def str_to_int(value):
    """
    Преобразовать значение к целочисленному типу и вернуть его.
    """
    return int(value)


def print_int(value):
    """
    Вывести значение на экран.
    """
    print(value)


def main():
    """
    Главная функция программы.
    """
    # Получить ввод с клавиатуры.
    input_value = get_input()

    # Проверить возможность преобразования к целому числу.
    if test_input(input_value):
        # Преобразовать значение к целочисленному типу.
        int_value = str_to_int(input_value)

        # Вывести полученное значение на экран.
        print_int(int_value)
    else:
        print("Введенное значение нельзя преобразовать к целому числу.")


if __name__ == '__main__':
    main()
