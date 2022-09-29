#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Пример сложной обработки командной строки, когда есть именнованный аргумент и значение.
"""
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Привет, мир!")
    else:
        if len(sys.argv) < 3:
            print("Ошибка. Слишком мало параметров.")
            sys.exit(1)

        if len(sys.argv) > 3:
            print("Ошибка. Слишком много параметров.")
            sys.exit(1)

        param_name = sys.argv[1]
        param_value = sys.argv[2]

        if (param_name == "--name" or
                param_name == "-n"):
            print(f"Привет, {param_value}!")
        else:
            print(f"Ошибка. Неизвестный параметр '{param_name}'")
            sys.exit(1)
