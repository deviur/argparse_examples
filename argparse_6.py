#!/usr/bin/python
# -*- coding: UTF-8 -*-

import argparse


def create_parser():
    p = argparse.ArgumentParser()
    p.add_argument('-g', '--goodbye', action='store_true', default=False)
    return p


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()

    print(f"Привет, мир!")
    if namespace.goodbye:
        print(f"Прощай, мир!")
