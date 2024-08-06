import math
from mathFunctionsBase import MathFunctions, Negate

class Sin(MathFunctions):
    def __call__(self, x):
        return round(math.sin(x), 2)
    
    def derivative(self):
        return Cos()
    
    def __str__(self):
        return "sin(x)"
    
class Cos(MathFunctions):
    def __call__(self, x):
        return round(math.cos(x), 2)
    
    def derivative(self):
        return -Sin()
    
    def __str__(self):
        return "cos(x)"