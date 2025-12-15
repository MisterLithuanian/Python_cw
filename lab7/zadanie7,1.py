from fracs import *
import unittest


class TestFrac(unittest.TestCase): 
	def setUp(self): 
		self.a = Frac(3,-2)
		self.b = Frac(7,1)
		self.c = Frac(5,2)
		self.d = Frac(2,2)
		self.e = Frac(7,3)
		self.f = Frac(4,7)

	def test_str(self):
		self.assertEqual( str(self.a), "-3/2" )
		self.assertEqual( str(self.d), "1" )

	def test_repr(self):
		self.assertEqual( repr(self.c), "Frac(5, 2)" )

	def test_eq(self):
		self.assertTrue( self.b == Frac(7) )
		self.assertTrue( self.d == 1 )

	def test_neq(self): 
		self.assertTrue( self.a != self.b )
		self.assertFalse( self.a != self.a )

	def test_lt(self):
		self.assertTrue( self.a < self.b )
		self.assertFalse( self.c < self.e )

	def test_le(self):
		self.assertTrue( Frac(7,1) <= self.b )
		self.assertTrue( Frac(7,2) <= self.b )

	def test_gt(self): 
		self.assertTrue ( self.e > self.f )


	def test_ge(self): 
		self.assertTrue( Frac(5,2) >= self.c )
		self.assertTrue( Frac(6,2) >= self.c )

	def test_add(self): 
		self.assertEqual( self.a+self.c, 1 )
		self.assertEqual( self.f+self.e, Frac(61,21))
		self.assertEqual( self.b+1, 8)
		self.assertEqual( 4+self.d, 5)

	def test_sub(self):
		self.assertEqual( self.f-self.e, Frac(-37,21))
		self.assertEqual( self.b-1, 6)
		self.assertEqual( 4-self.d, 3)

	def test_mul(self):
		self.assertEqual( self.b*self.f, 4)
		self.assertEqual( self.a*(-2), 3 )

	def test_div(self):
		self.assertEqual( self.e/self.b, Frac(1,3) )
		self.assertEqual( float(self.a/3), -0.5 )
		self.assertEqual( 3/self.c, Frac(6,5) )

	def test_pos(self):
		self.assertEqual( +self.a, Frac(-3,2) )

	def test_neg(self):
		self.assertEqual( -self.a, Frac(3,2) )

	def test_invert(self):
		self.assertEqual( ~self.b, Frac(1,7) )

	def test_float(self):
		self.assertEqual( float(self.c), 2.5 )
		self.assertEqual( float(self.d), 1.0 )

	def test_hash(self): 
		self.assertTrue( set([2]) == set([Frac(2)]) )

	def tearDown(self): 
		del self.a
		del self.b
		del self.c
		del self.d
		del self.e
		del self.f 

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy