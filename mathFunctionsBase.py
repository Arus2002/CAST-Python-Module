import math
from abc import ABC, abstractmethod

class MathFunctions(ABC):
    @abstractmethod
    def __call__(self, x):
        pass

    @abstractmethod
    def derivative(self):
        pass
