from dataclasses import dataclass
@dataclass(frozen=True)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def length(self):
        return (self.x**2 + self.y**2)**0.5

    def __hash__(self):
        return hash((self.x, self.y))




class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]"

    def __repr__(self):
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):
        return not self == other

    def center(self):
        return Point(
            (self.pt1.x+self.pt2.x)/2,
            (self.pt1.y+self.pt2.y)/2
        )

    def area(self):
        return abs(self.pt2.x-self.pt1.x)*abs(self.pt2.y-self.pt1.y)

    def move(self, x, y):
        self.pt1 = Point(self.pt1.x + x, self.pt1.y + y)
        self.pt2 = Point(self.pt2.x + x, self.pt2.y + y)
        return self
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
