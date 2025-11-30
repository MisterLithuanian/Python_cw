import unittest
from rectangles import Rectangle
from points import Point

class TestRectangle(unittest.TestCase):

    def test_str(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(str(r), "[(1, 2), (3, 4)]")

    def test_repr(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(repr(r), "Rectangle(1, 2, 3, 4)")

    def test_eq(self):
        self.assertTrue(Rectangle(1, 2, 3, 4) == Rectangle(1, 2, 3, 4))
        self.assertFalse(Rectangle(1, 2, 3, 4) == Rectangle(1, 1, 3, 4))

    def test_ne(self):
        self.assertTrue(Rectangle(0, 0, 1, 1) != Rectangle(0, 0, 2, 2))

    def test_center(self):
        r = Rectangle(0, 0, 4, 4)
        self.assertEqual(r.center(), Point(2, 2))

    def test_area(self):
        self.assertEqual(Rectangle(0, 0, 4, 5).area(), 20)

    def test_move(self):
        r = Rectangle(1, 2, 3, 4)
        r.move(10, -2)
        self.assertEqual(r, Rectangle(11, 0, 13, 2))

if __name__ == "__main__":
    unittest.main()