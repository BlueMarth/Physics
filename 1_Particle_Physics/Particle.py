import math
import numbers
import operator
from typing import NamedTuple, Tuple
import Vector2 as Vec2


class Particle():

    mass: float
    
    @property
    def inverseMass(self):
        if self.mass <=0:
            return 0
        else:
            return 1 / self.mass
    
    @property
    def position(self, time) -> Tuple[float,float]:
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

    def integrate(self, dt):
        assert dt > 0.0
        self.position.addScaledVector(velocity, duration)
    

