from .mathFunctionsBase import MathFunctions
import math
from cos import Cos
from operations import Negate

class Sin(MathFunctions):
    def __call__(self, x):
        return math.sin(x)
        
    def __neg__(self):
        return Negate(self)
    
    def derivative(self):
        return Cos()