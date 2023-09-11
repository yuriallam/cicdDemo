import unittest
from xmlrunner import XMLTestRunner

from main import add

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

if __name__ == "__main__":
     unittest.main(testRunner=XMLTestRunner(output='test-reports', outsuffix='test-report2'))
