import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        # Positive numbers
        self.assertEqual(self.calc.add(5, 7), 12)
        # Negative numbers
        self.assertEqual(self.calc.add(-3, -8), -11)
        # Mixed numbers
        self.assertEqual(self.calc.add(10, -4), 6)
        self.assertEqual(self.calc.add(-5, 9), 4)
        # Zero
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(7, 0), 7)
        # Large numbers
        self.assertEqual(self.calc.add(1_000_000_000, 2_000_000_000), 3_000_000_000)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(-10, -4), -6)
        self.assertEqual(self.calc.subtract(5, -3), 8)
        self.assertEqual(self.calc.subtract(-5, 3), -8)
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(7, 7), 0)
        self.assertEqual(self.calc.subtract(2_000_000_000, 1_000_000_000), 1_000_000_000)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(3, 7), 21)
        self.assertEqual(self.calc.multiply(-4, -6), 24)
        self.assertEqual(self.calc.multiply(-5, 6), -30)
        self.assertEqual(self.calc.multiply(5, -6), -30)
        self.assertEqual(self.calc.multiply(7, 0), 0)
        self.assertEqual(self.calc.multiply(0, 7), 0)
        self.assertEqual(self.calc.multiply(9, 1), 9)
        self.assertEqual(self.calc.multiply(1, 9), 9)
        self.assertEqual(self.calc.multiply(1_000_000, 2_000_000), 2_000_000_000_000)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-12, -3), 4)
        self.assertEqual(self.calc.divide(-15, 3), -5)
        self.assertEqual(self.calc.divide(15, -3), -5)
        self.assertEqual(self.calc.divide(9, 1), 9)
        self.assertEqual(self.calc.divide(-7, 1), -7)
        self.assertEqual(self.calc.divide(8, 8), 1)
        self.assertEqual(self.calc.divide(-5, -5), 1)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)
        self.assertAlmostEqual(self.calc.divide(10, 4), 2.5)
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(-7, 0))
        self.assertEqual(self.calc.divide(2_000_000_000, 2_000_000), 1000)

if __name__ == "__main__":
    unittest.main()