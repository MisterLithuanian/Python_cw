from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: float
    y: float


class Rectangle:
    def __init__(self, x: float, y: float, width: float, height: float):
        if width < 0 or height < 0:
            raise ValueError("Wartości muszą być dodatnie")
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    @classmethod
    def from_points(cls, points):
        p1, p2 = points
        x1, y1 = p1
        x2, y2 = p2

        left = min(x1, x2)
        right = max(x1, x2)
        bottom = min(y1, y2)
        top = max(y1, y2)

        return cls(left, bottom, right - left, top - bottom)

    @property
    def left(self):
        return self._x

    @property
    def bottom(self):
        return self._y

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def right(self):
        return self._x + self._width

    @property
    def top(self):
        return self._y + self._height

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def center(self):
        return Point(
            self.left + self.width / 2,
            self.bottom + self.height / 2
        )
