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
    
    def __neg__(self):
        return Negate(self)
    
class Negate(MathFunctions):
    def __init__(self, f):
        self._f = f

    def __call__(self, x):
        return round(-self._f(x), 2)

    def derivative(self):
        return -self._f.derivative()
    
    def __str__(self):
        return f"(-{self._f})"
    
class Sum(MathFunctions):
    def __init__(self, f, g):
        self._f = f
        self._g = g
    
    def __call__(self, x):
        return round(self._f(x) + self._g(x), 2)
    
    def derivative(self):
        return self._f.derivative() + self._g.derivative()
    
    def __str__(self):
        return f"({self._f} + {self._g})"

class Sub(MathFunctions):
    def __init__(self, f, g):
        self._f = f
        self._g = g
    
    def __call__(self, x):
        return round(self._f(x) - self._g(x), 2)
    
    def derivative(self):
        return self._f.derivative() - self._g.derivative()
    
    def __str__(self):
        return f"({self._f} - {self._g})"

class Mul(MathFunctions):
    def __init__(self, f, g):
        self._f = f
        self._g = g
    
    def __call__(self, x):
        return round(self._f(x) * self._g(x), 2)
    
    def derivative(self):
        return (self._f.derivative() * self._g) + (self._f * self._g.derivative())
    
    def __str__(self):
        return f"({self._f} * {self._g})"

class Div(MathFunctions):
    def __init__(self, f, g):
        self._f = f
        self._g = g
    
    def __call__(self, x):
        return round(self._f(x) / self._g(x), 2)
    
    def derivative(self):
        return ((self._f.derivative() * self._g) - (self._f * self._g.derivative())) / (self._g * self._g)
    
    def __str__(self):
        return f"({self._f} / {self._g})"

class Compose(MathFunctions):
    def __init__(self, f, g):
        self._f = f
        self._g = g
    
    def __call__(self, x):
        return round(self._f(self._g(x)), 2)
    
    def derivative(self):
        return (self._f.derivative().apply(self._g) * self._g.derivative())
    
    def __str__(self):
        outer_func = str(self._f)
        inner_func = str(self._g)
        return outer_func.replace('x', f"({inner_func})")
    
