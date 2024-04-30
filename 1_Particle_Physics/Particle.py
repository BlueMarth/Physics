import math
import numbers
import operator
from typing import NamedTuple, Tuple
import Vector2 as Vec2

class Particle():

    @property
    def position(self) -> Tuple[float,float]:
        pass

    @property
    def velocity(self) -> Vec2:
        pass

    @property
    def acceleration(self) -> Vec2:
        pass

    @property
    def damping(self) -> float:
        pass

    @property
    def inverseMass(self) -> float:
        pass

