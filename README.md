# argparse_examples
Examples of how to use the argparse python library
## Run all tests
```
python -m unittest
```
## Files:
___
### no_argparse.py
Пример обработки аргументов командной строки без библиотеки argparse.
#### Usage:
```
python3 no_argparse.py
python3 no_argparse.py Денис
```
___
### no_argparse_2.py
Пример обработки сложных аргументов командной строки без argparse.
Тут используется именованный аргумент `--name (-n)` и значение имени.
#### Usage:
```
python3 no_argparse_2.py
python3 no_argparse_2.py --name Денис
```
___
### argparse_1.py
Пример для одного необязательного аргумента `name`
#### Usage:
```
python3 argparse_1.py [-h] [name]
```
#### Source:
```
parser.add_argument('name', nargs='?')
namespace = parser.parse_args()
print(namespace.name)
```
___
### argparse_2.py
Пример синонимов для одного необязательного аргумента `name`
#### Usage:
```
python3 argparse_2.py [-h] [-n NAME]
```
#### Source:
```
parser.add_argument('-n', '--name', '--username')
namespace = parser.parse_args()
print(namespace.name)
```
___
### argparse_3.py
Пример использования значения по умолчанию
#### Usage:
```
python3 argparse_3.py [-h] [-n NAME]
```
#### Source:
```
parser.add_argument('-n', '--name', default='мир')
namespace = parser.parse_args()
print(namespace.name)
```
___
### argparse_4.py
Пример использования списка значений в качестве аргумента.
#### Usage:
```
python3 argparse_4.py [-h] [-n NAME [NAME ...]]
```
#### Source:
```
parser.add_argument('-n', '--name', nargs='+', default=['мир'])
namespace = parser.parse_args()
print(namespace.name)
```
___
### argparse_5.py
Пример, выбор одного значения из нескольких вариантов.
#### Usage:
```
python3 argparse_5.py [-h]  [-n {мир,Денис,Вася,Николай}]
```
#### Source:
```
parser.add_argument('-n', '--name', choices=['мир', 'Денис', 'Вася', 'Николай'], default='мир')
namespace = parser.parse_args()
print(namespace.name)
```
___
### argparse_6.py
Пример параметров в качестве флагов.
#### Usage:
```
python3 argparse_6.py [-h] [-g]
```
#### Source:
```
parser.add_argument('-g', '--goodbye', action='store_true', default=False)
namespace = parser.parse_args()
print(namespace.name)
```
___
### argparse_7.py
Пример использования подпарсеров.
#### Usage:
```
python3 argparse_7.py [-h]  {hello,goodbye} ...
python3 argparse_7.py hello [-h] names [names ...]
python3 argparse_7.py goodbye [-h] [-c COUNT]
```
#### Source:
```
subparsers = p.add_subparsers(dest='command')

hello_parser = subparsers.add_parser('hello')
hello_parser.add_argument('names', nargs='+', default=['мир'])

goodbye_parser = subparsers.add_parser('goodbye')
goodbye_parser.add_argument('-c', '--count', type=int, default=1)

namespace = parser.parse_args()
print(namespace.name)
```
