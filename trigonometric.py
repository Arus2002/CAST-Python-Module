from mathFunctionsBase import MathFunctions, Negate
import math

class Sin(MathFunctions):
    def __call__(self, x):
        return round(math.sin(x), 2)
        
    def __neg__(self):
        return Negate(self)
    
    def derivative(self):
        return Cos()
    
class Cos(MathFunctions):
    def __call__(self, x):
        return round(math.cos(x), 2)
    
    def derivative(self):
        return -Sin()