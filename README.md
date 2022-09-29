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
