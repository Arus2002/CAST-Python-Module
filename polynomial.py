from .mathFunctionsBase import MathFunctions

class Polynomial(MathFunctions):
    def __init__(self, *coefficients):
        self.coefficients = coefficients
    
    def __call__(self, x):
        result = 0
        for i, coeff in enumerate(self.coefficients):
            result += coeff * (x ** i)
        return result
    
    def derivative(self): 
        deriv_coeffs = []
        for i, coef in enumerate(self.coefficients):
            if i > 0:  # Skip the constant term (index 0)
                deriv_coeffs = i * coef
                deriv_coeffs.append(deriv_coeffs)

        return Polynomial(deriv_coeffs)