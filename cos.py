from .mathFunctionsBase import MathFunctions
import math
from sin import Sin

class Cos(MathFunctions):
    def __call__(self, x):
        return math.cos(x)
    
    def derivative(self):
        return -Sin()