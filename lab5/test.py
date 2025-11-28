import unittest
from fracs import *

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([2, 3], [1, 3]), [9, 9])

    def test_sub_frac(self): 
        self.assertEqual(sub_frac([2,3], [1,3]), [3,9])

    def test_mul_frac(self): 
        self.assertEqual(mul_frac([2,3], [1,3]), [2,9])

    def test_div_frac(self): 
        self.assertEqual(div_frac([2,3], [1,3]), [6,3])

    def test_is_positive(self): 
        self.assertEqual(is_positive([2,3]), True)

    def test_is_zero(self): 
        self.assertEqual(is_zero(self.zero), True)

    def test_cmp_frac(self): 
        self.assertEqual(cmp_frac([2,3], [1,3]), 1)

    def test_frac2float(self): 
        self.assertEqual(frac2float([1,8]), 0.125)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy