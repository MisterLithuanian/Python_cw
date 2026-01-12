import pytest
from rectangles import Rectangle, Point


def test_from_points():
    r = Rectangle.from_points(((1, 2), (5, 6)))
    assert r.left == 1
    assert r.bottom == 2
    assert r.width == 4
    assert r.height == 4


def test_edges():
    r = Rectangle(0, 0, 10, 5)
    assert r.right == 10
    assert r.top == 5


def test_corners():
    r = Rectangle(1, 2, 3, 4)
    assert r.bottomleft == Point(1, 2)
    assert r.topleft == Point(1, 6)
    assert r.bottomright == Point(4, 2)
    assert r.topright == Point(4, 6)


def test_center():
    r = Rectangle(0, 0, 10, 10)
    assert r.center == Point(5, 5)


def test_invalid_dimensions():
    with pytest.raises(ValueError):
        Rectangle(0, 0, -1, 5)


def test_from_points_invalid():
    with pytest.raises(ValueError):
        Rectangle.from_points(((0, 0),))
