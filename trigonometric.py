from mathFunctionsBase import MathFunctions, Negate
import math

class Sin(MathFunctions):
    def __call__(self, x):
        return math.sin(x)
        
    def __neg__(self):
        return Negate(self)
    
    def derivative(self):
        return Cos()
    
class Cos(MathFunctions):
    def __call__(self, x):
        return math.cos(x)
    
    def derivative(self):
        return -Sin()