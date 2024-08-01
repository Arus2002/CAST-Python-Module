import math
from abc import ABC, abstractmethod

class MathFunctions(ABC):
    @abstractmethod
    def __call__(self, x):
        pass

    @abstractmethod
    def derivative(self):
        pass

    def apply(self, other):
        return Compose(self, other)

    def __add__(self, other):
        return Sum(self, other)

    def __sub__(self, other):
        return Sub(self, other)

    def __mul__(self, other):
        return Mul(self, other)

    def __truediv__(self, other):
        return Div(self, other)
    
class Negate(MathFunctions):
    def __init__(self, f):
        self._f = f

    def __call__(self, x):
        return round(-self._f(x), 2)

    def derivative(self):
        return -self._f.derivative()
    
class Sum(MathFunctions):
    def __init__(self, f, g):
        self._f = f
        self._g = g
    
    def __call__(self, x):
        return round(self._f(x) + self._g(x), 2)
    
    def derivative(self):
        return Sum(self._f.derivative(), self._g.derivative())

class Sub(MathFunctions):
    def __init__(self, f, g):
        self._f = f
        self._g = g
    
    def __call__(self, x):
        return round(self._f(x) - self._g(x), 2)
    
    def derivative(self):
        return Sub(self._f.derivative(), self._g.derivative())

class Mul(MathFunctions):
    def __init__(self, f, g):
        self._f = f
        self._g = g
    
    def __call__(self, x):
        return round(self._f(x) * self._g(x), 2)
    
    def derivative(self):
        return Sum(Mul(self._f.derivative(), self._g), Mul(self._f, self._g.derivative()))

class Div(MathFunctions):
    def __init__(self, f, g):
        self._f = f
        self._g = g
    
    def __call__(self, x):
        return round(self._f(x) / self._g(x), 2)
    
    def derivative(self):
        return Div(Sub(Mul(self._f.derivative(), self._g), Mul(self._f, self._g.derivative())), Mul(self._g, self._g))

class Compose(MathFunctions):
    def __init__(self, f, g):
        self._f = f
        self._g = g
    
    def __call__(self, x):
        return round(self._f(self._g(x)), 2)
    
    def derivative(self):
        return Mul(self._f.derivative().apply(self._g), self._g.derivative())
    
