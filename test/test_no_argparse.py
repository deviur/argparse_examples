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


if __name__ == '__main__':
    unittest.main()
