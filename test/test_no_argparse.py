import unittest
import subprocess


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_no_argparse(self):
        output = subprocess.getoutput('python3 no_argparse.py')
        self.assertEqual(output, 'Привет, мир!')

        output = subprocess.getoutput('python3 no_argparse.py Денис')
        self.assertEqual(output, 'Привет, Денис!')

        output = subprocess.getoutput('python3 no_argparse.py Денис Великолепный III')
        self.assertEqual(output, 'Привет, Денис!')

    def test_no_argparse_2(self):
        output = subprocess.getoutput('python3 no_argparse_2.py')
        self.assertEqual(output, 'Привет, мир!')

        output = subprocess.getoutput('python3 no_argparse_2.py Денис')
        self.assertEqual(output, 'Ошибка. Слишком мало параметров.')

        output = subprocess.getoutput('python3 no_argparse_2.py Денис Великолепный III')
        self.assertEqual(output, 'Ошибка. Слишком много параметров.')

        output = subprocess.getoutput('python3 no_argparse_2.py --name Денис')
        self.assertEqual(output, 'Привет, Денис!')

        output = subprocess.getoutput('python3 no_argparse_2.py -n Денис')
        self.assertEqual(output, 'Привет, Денис!')

        output = subprocess.getoutput('python3 no_argparse_2.py --name Денис')
        self.assertEqual(output, 'Привет, Денис!')

        output = subprocess.getoutput('python3 no_argparse_2.py -h Денис')
        self.assertEqual(output, "Ошибка. Неизвестный параметр '-h'")


if __name__ == '__main__':
    unittest.main()
