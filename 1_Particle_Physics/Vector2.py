import math
import numbers
import operator
from typing import NamedTuple, Tuple

class Vector2(NamedTuple):
    
    x: float
    y: float

    @property
    def length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)
    
    def get_length_sqrd(self) -> float:
        return self.x**2 + self.y**2

    @property
    def angle(self) -> float:
        if self.get_length_sqrd() == 0:
            return 0
        return math.atan2(self.y, self.x)
    
    @property
    def angle_degrees(self) -> float:
        return math.degrees(self.angle)
    
    def __add__(self, other: Tuple[float, float]) -> "Vector2":
        assert (len(other) == 2), f"{other} not supported. Only Vector2 and Sequence of length 2 is supported"
        return Vector2(self.x + other[0], self.y + other[1])

    def __sub__(self, other: Tuple[float, float]) -> "Vector2":
        assert (len(other) == 2), f"{other} not supported. Only Vector2 and Sequence of length 2 is supported"
        return Vector2(self.x - other[0], self.y - other[1])
    
    def __mul__(self, other: float) -> "Vector2":
        assert isinstance(other, numbers.Real)
        return Vector2(self.x * other, self.y * other)

    def __div__(self, other) -> "Vector2":
        assert isinstance(other, numbers.Real)
        return Vector2(self.x / other, self.y / other)
    
    
    # vector-vector or vector-scaler functions
    def get_angle_between(self, other: Tuple[float, float]) -> float:
        num = self.__dot_product__(self, other)
        den = math.sqrt(self.x**2 + self.y**2) * math.sqrt(other[0]**2+other[1]**2)
        return math.acos(num/den)

    def get_angle_degrees_between(self) -> float:
        return math.degrees(self.get_angle_between)
    
    def scale_to_length(self, other: float) -> "Vector2":
        old_length = self.length
        return Vector2(self.x * other / old_length, self.y * other / old_length)
    
    def rotated(self, angle_radians: float) -> "Vector2":
        cos = math.cos(angle_radians)
        sin = math.sin(angle_radians)
        x = self.x * cos - self.y * sin
        y = self.x * sin + self.y * cos
        return Vector2(x, y)
    
    def rotated_degrees(self, angle_degrees) -> "Vector2":
        return self.rotated(math.radians(angle_degrees))
    
    def normalized(self) -> "Vector2":
        length = self.length
        if length != 0:
            return self / length
        return Vector2(0, 0)
    
    def perpendicular(self) -> "Vector2":
        return Vector2(-self.y, self.x)
    
    def dot(self, other: Tuple[float, float]) -> float:
        assert len(other) == 2
        return math.sqrt(self.x * other[0] + self.y * other[1])
    
    def cross(self, other: Tuple[float,float]) -> float:
        assert len(other) == 2
        return self.x * other[1] - self.y * other[0]
    
    def get_distance(self, other: Tuple[float, float]) -> float:
        assert len(other) == 2
        return math.sqrt((self.x - other[0])**2 + (self.y - other[1])**2)
    
    def projection(self, other: Tuple[float, float]) -> "Vector2":
        assert len(other) == 2
        other_length_sqrd = other[0]**2 + other[1]**2
        if other_length_sqrd == 0.0:
            return Vector2(0 ,0)
        projected_length_times_other_length = self.dot(other)
        new_length = projected_length_times_other_length / other_length_sqrd
        return Vector2(other[0] * new_length, other[1] * new_length)


    # unary operations
    def __neg__(self) -> "Vector2":
        return -self.x, -self.y
    
    def __pos__(self) -> "Vector2":
        return Vector2(operator.pos(self.x), operator.pos(self.y))
    
    def __abs__(self) -> "Vector2":
        return self.length
    
