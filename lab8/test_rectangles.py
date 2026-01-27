import pytest
from rectangles import Rectangle
from points import Point


def test_from_points():
    p1 = Point(1, 2)
    p2 = Point(5, 6)
    r = Rectangle.from_points((p1, p2))
    assert r.pt1 == p1
    assert r.pt2 == p2


def test_dimensions():
    r = Rectangle(1, 2, 5, 6)
    assert r.width == 4
    assert r.height == 4


def test_edges():
    r = Rectangle(1, 2, 5, 6)
    assert r.left == 1
    assert r.right == 5
    assert r.bottom == 2
    assert r.top == 6


def test_corners():
    r = Rectangle(1, 2, 5, 6)
    assert r.topleft == Point(1, 6)
    assert r.topright == Point(5, 6)
    assert r.bottomleft == Point(1, 2)
    assert r.bottomright == Point(5, 2)


def test_center():
    r = Rectangle(0, 0, 4, 4)
    assert r.center == Point(2, 2)


def test_area():
    r = Rectangle(0, 0, 4, 5)
    assert r.area() == 20


def test_move():
    r = Rectangle(1, 1, 3, 3)
    r.move(2, 3)
    assert r.pt1 == Point(3, 4)
    assert r.pt2 == Point(5, 6)


def test_equality():
    r1 = Rectangle(1, 2, 3, 4)
    r2 = Rectangle(1, 2, 3, 4)
    r3 = Rectangle(0, 0, 3, 4)
    assert r1 == r2
    assert r1 != r3
