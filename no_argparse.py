#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Пример обработки аргументов командной строки без библиотеки argparse
"""
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(f"Привет, {sys.argv[1]}!")
    else:
        print("Привет, мир!")
