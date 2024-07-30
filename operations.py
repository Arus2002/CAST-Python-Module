from .mathFunctionsBase import MathFunctions

class Negate(MathFunctions):
    def __init__(self, f):
        self.f = f

    def __call__(self, x):
        return -self.f(x)

    def derivative(self):
        return -self.f.derivative()