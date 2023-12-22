import unittest
from exprogram import calculate

class Test(unittest.TestCase):

    def test_calculate_scholarship(self):
        result = calculate(80, 100, 500)
        self.assertEqual(result, 40000) 

        result = calculate(90, 100, 300)
        self.assertEqual(result, 27000) 

    def test_calculate_scholarship_with_mixed_types(self):
        with self.assertRaises(TypeError):
            result = calculate('abc', 'def', 'ghi')


if __name__ == '__main__':

    unittest.main()