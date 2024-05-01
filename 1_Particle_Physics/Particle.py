import math
import numbers
import operator
from typing import NamedTuple, Tuple
import Vector2 as Vec2


class Particle():

    mass: float
    
    @property
    def position(self) -> Tuple[float,float]:
        pass

    @property
    def velocity(self) -> Vec2:
        pass

    @property
    def acceleration(self, force_applied: Vec2) -> Vec2:
        assert self.inverseMass > 0
        return self.inverseMass * force_applied

    @property
    def damping(self) -> float:
        pass

    @property
    def inverseMass(self) -> float:
        pass

    

