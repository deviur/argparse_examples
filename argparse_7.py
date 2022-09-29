#!/usr/bin/python
# -*- coding: UTF-8 -*-

import argparse


def create_parser():
    p = argparse.ArgumentParser()
    subparsers = p.add_subparsers(dest='command')

    hello_parser = subparsers.add_parser('hello')
    hello_parser.add_argument('names', nargs='+', default=['мир'])

    goodbye_parser = subparsers.add_parser('goodbye')
    goodbye_parser.add_argument('-c', '--count', type=int, default=1)

    p.set_defaults(command='hello', names=['мир'])
    return p


def hello(namespace):
    """
    Выполнение команды hello
    """
    for name in namespace.names:
        print(f"Привет, {name}!")


def goodbye(namespace):
    """
    Выполнение команды goodbye
    """
    for _ in range(namespace.count):
        print("Прощай, мир!")


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()

    print(namespace)

    if namespace.command == 'hello':
        hello(namespace)
    if namespace.command == 'goodbye':
        goodbye(namespace)
