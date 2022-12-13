import unittest
import calculator
class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(10,5),15)
        self.assertEqual(calculator.add(-1,5),4)
        self.assertEqual(calculator.add(-4,-5),-9)

    def test_subtract(self):
            self.assertEqual(calculator.subtract(10,5),4)
            self.assertEqual(calculator.subtract(-1,5),-6)
            self.assertEqual(calculator.subtract(-4,-5),1)

    def test_multiply(self):
            self.assertEqual(calculator.multiply(10,5),15)
            self.assertEqual(calculator.multiply(-1,5),-5)
            self.assertEqual(calculator.multiply(-4,-5),20)
            self.assertEqual(calculator.multiply(1,-5),-5)

unittest.main(argv=[''], verbosity=2, exit=False)



