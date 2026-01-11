from fracs import *
import unittest


class TestFrac(unittest.TestCase): 
	def setUp(self): 
		self.a = Frac(4, 3)
		self.b = Frac(4, 1)
		self.c = Frac(-4, 3)
		self.d = Frac(1 ,2)
	def test_str(self):
		self.assertEqual(str(self.a), "4/3")
		self.assertEqual(str(self.b), "4")
	def test_repr(self):
		self.assertEqual(repr(self.a), "Frac(4, 3)")
	def test_eq(self):
		self.assertFalse(self.a.__eq__(self.b))
		self.assertFalse(self.a == self.b)
	def test_neq(self): 
		self.assertTrue(self.a!=self.b)
	def test_lt(self):
		self.assertTrue(self.a<self.b)
	def test_le(self):
		self.assertTrue(self.a<=self.b)
	def test_gt(self): 
		self.assertFalse(self.a>self.b)
	def test_ge(self): 
		self.assertFalse(self.a>=self.b)
	def test_add(self): 
		self.assertEqual(self.a+self.b, Frac(16, 3))
	def test_sub(self):
		self.assertEqual(self.b-self.a, Frac(8, 3))
	def test_mul(self):
		self.assertEqual(self.a*self.b, Frac(16, 3))
	def test_div(self):
		self.assertEqual(self.a/self.b, Frac(1, 3))
	def test_pos(self):
		self.assertEqual(+self.c, Frac(-4, 3))
	def test_neg(self):
		self.assertEqual(-self.c, Frac(4, 3))
	def test_invert(self):
		self.assertEqual(~self.a, Frac(3, 4))
	def test_float(self):
		self.assertEqual(float(self.d), 0.5)
	def test_hash(self): 
		pass
	def tearDown(self): 
		del self.a 
		del self.b

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy