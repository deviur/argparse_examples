#!/usr/bin/python
# -*- coding: UTF-8 -*-

import argparse


def create_parser():
    p = argparse.ArgumentParser()
    p.add_argument('-n', '--name', nargs='+', default=['мир'])
    return p


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()

    for name in namespace.name:
        print(f"Привет, {name}!")
