#!/usr/bin/python
# -*- coding: UTF-8 -*-

import argparse


def create_parser():
    p = argparse.ArgumentParser()
    p.add_argument('-n', '--name', '--username')
    return p


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()

    if namespace.name:
        print(f"Привет, {namespace.name}!")
    else:
        print("Привет, мир!")
