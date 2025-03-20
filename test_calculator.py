import unittest
from calculator import calculator

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator('2+3'), 5)
    
    def test_subtraction(self):
        self.assertEqual(calculator('5-2'), 3)
    
    def test_multiplication(self):
        self.assertEqual(calculator('2*3'), 6)
    
    def test_division(self):
        self.assertEqual(calculator('6/2'), 3)
    
    def test_mixed_operations(self):
        self.assertEqual(calculator('2+3*4'), 14)
        self.assertEqual(calculator('8/2-3'), 1)

if __name__ == '__main__':
    unittest.main()
