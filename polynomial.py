from mathFunctionsBase import MathFunctions

class Polynomial(MathFunctions):
    def __init__(self, *coefficents):
        self._coefficents = coefficents
    
    @property
    def coefficents(self):
        return self._coefficents
        
    @coefficents.setter
    def coefficents(self, *coefficents):
        self._coefficents = coefficents

    def __call__(self, x):
        result = 0
        for i, coef in enumerate(self._coefficents):
            result += coef * (x ** i)
        return round(result, 2)
    
    def derivative(self): 
        der_coeffs = []
        for i, coef in enumerate(self._coefficents):
            if i > 0:
                deriv_coef__f = i * coef
                der_coeffs.append(deriv_coef__f)

        return Polynomial(*der_coeffs)
