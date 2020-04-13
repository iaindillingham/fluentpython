from math import hypot


class Vector:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return 'Vector({}, {})'.format(self.x, self.y)

    def __abs__(self) -> float:
        return hypot(self.x, self.y)

    def __bool__(self) -> bool:
        return bool(abs(self))

    def __add__(self, other: 'Vector') -> 'Vector':
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar: float) -> 'Vector':
        x = self.x * scalar
        y = self.y * scalar
        return Vector(x, y)
