from fracs import *
import unittest


class TestFrac(unittest.TestCase): 
	def setUp(self): 
		self.a = Frac(4, 3)
		self.b = Frac(4, 1)

	def test_str(self):
		self.assertEqual(str(self.a), "4/3")
		self.assertEqual(str(self.b), "4")
	def test_repr(self):
		self.assertEqual(repr(self.a), "Frac(4, 3)")
	def test_eq(self):
		self.assertFalse(self.a.__eq__(self.b))
		self.assertFalse(self.a == self.b)
	def test_neq(self): 
		pass
	def test_lt(self):
		pass
	def test_le(self):
		pass
	def test_gt(self): 
		pass
	def test_ge(self): 
		pass
	def test_add(self): 
		pass
	def test_sub(self):
		pass
	def test_mul(self):
		pass
	def test_div(self):
		pass
	def test_pos(self):
		pass
	def test_neg(self):
		pass
	def test_invert(self):
		pass
	def test_float(self):
		pass
	def test_hash(self): 
		pass
	def tearDown(self): 
		del self.a 
		del self.b

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy