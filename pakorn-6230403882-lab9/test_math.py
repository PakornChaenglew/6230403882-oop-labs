import unittest
import math2


class TestMath(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(math2.sum(1, 2), 3)
        self.assertEqual(math2.sum(1.1, 2.3), 3.4)

    def test_subtract(self):
        self.assertEqual(math2.subtract(10, 2), 8)
        self.assertEqual(math2.subtract(-3, 2), -5)

    def test_mul(self):
        self.assertEqual(math2.mul(2, 3), 6)
        self.assertEqual(math2.mul(-1, -2), 2)

    def test_divide(self):
        self.assertEqual(math2.divide(10, 2), 5)
        self.assertEqual(math2.divide(3, 2), 1.5)
        self.assertRaises(ValueError, math2.divide, 12, 0)

if __name__ == '__main__':
    unittest.main()