import unittest
from main import codacy


class MyTestCase(unittest.TestCase):
    def test_codacy(self):
        self.assertEqual(codacy(), 'hello')  # add assertion here


if __name__ == '__main__':
    unittest.main()
