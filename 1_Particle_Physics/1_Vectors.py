import math
import numbers
import operator
from typing import NamedTuple, Tuple

class Vec2d(NamedTuple):
    
    x: float
    y: float

    
    
    def __add__(self, other: Tuple[float, float]) -> "Vec2d":
        assert (len(other) == 2), f"{other} not supported. Only Vec2d and Sequence of length 2 is supported"
        return Vec2d(self.x + other[0], self.y + other[1])

    def __sub__(self, other: Tuple[float, float]) -> "Vec2d":
        assert (len(other) == 2), f"{other} not supported. Only Vec2d and Sequence of length 2 is supported"
        return Vec2d(self.x - other[0], self.y - other[1])
    
    def __dot__(self, other: Tuple[float, float]) -> float:
        assert len(other) == 2
        return math.sqrt(self.x * other[0] + self.y * other[1])
        
    @property
    def __mag__(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)
    
    @property
    def angle(self) -> float:
        if self.get_length_sqrd() == 0:
            return 0
        return math.atan2(self.y, self.x)
    
    @property
    def angle_degrees(self) -> float:
        return math.degrees(self.angle)
    
    def get_angle_between(self, other: Tuple[float, float]) -> float:
        num = self.x * other[0] + self.y * other[1]
        den = math.sqrt(self.x**2 + self.y**2) * math.sqrt(other[0]**2+other[1]**2)
        return math.acos(num/den)

    def get_angle_degrees_between(self) -> float:
        return math.degrees(self.get_angle_between)