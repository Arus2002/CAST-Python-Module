import math
from abc import ABC, abstractmethod

class MathFunctions(ABC):
    @abstractmethod
    def __call__(self, x):
        pass

    @abstractmethod
    def derivative(self):
        pass
    
class Negate(MathFunctions):
    def __init__(self, f):
        self._f = f

    def __call__(self, x):
        return -self._f(x)

    def derivative(self):
        return -self._f.derivative()
    
