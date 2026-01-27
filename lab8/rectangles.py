from points import Point


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


    @classmethod
    def from_points(cls, points):
        p1, p2 = points
        return cls(p1.x, p1.y, p2.x, p2.y)


    @property
    def left(self):
        return min(self.pt1.x, self.pt2.x)

    @property
    def right(self):
        return max(self.pt1.x, self.pt2.x)

    @property
    def bottom(self):
        return min(self.pt1.y, self.pt2.y)

    @property
    def top(self):
        return max(self.pt1.y, self.pt2.y)

    @property
    def width(self):
        return self.right - self.left

    @property
    def height(self):
        return self.top - self.bottom


    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)

    @property
    def center(self):
        return Point(
            (self.left + self.right) / 2,
            (self.bottom + self.top) / 2
        )


    def area(self):
        return self.width * self.height

    def move(self, x, y):
        self.pt1 = Point(self.pt1.x + x, self.pt1.y + y)
        self.pt2 = Point(self.pt2.x + x, self.pt2.y + y)
        return self
