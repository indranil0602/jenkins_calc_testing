import unittest
from unittest import result
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(10, -5), 5)
        self.assertEqual(calc.add(-5, -5), -10)

    def test_substruct(self):
        self.assertEqual(calc.substruct(10, 5), 5)
        self.assertEqual(calc.substruct(10, -5), 15)
        self.assertEqual(calc.substruct(-5, -5), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(10, -5), -50)
        self.assertEqual(calc.multiply(-5, -5), 25)
        self.assertEqual(calc.multiply(10, 0), 0)

    def test_divison(self):
        self.assertEqual(calc.divison(10, 5), 2)
        self.assertEqual(calc.divison(1, -1), -1)
        self.assertEqual(calc.divison(-1, -1), 1)
        self.assertEqual(calc.divison(5, 2), 2.5)

        with self.assertRaises(ValueError):
            calc.divison(10, 0)

    def test_modulo(self):
        self.assertEqual(calc.modulo(11, 5), 1)
        self.assertEqual(calc.modulo(10, 5), 0)
        self.assertEqual(calc.modulo(-11, 5), 4)
        self.assertEqual(calc.modulo(11, -5), -4)

if __name__ == '__main__':
    unittest.main()