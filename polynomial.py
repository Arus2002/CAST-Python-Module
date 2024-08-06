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
                deriv_coeff = i * coef
                der_coeffs.append(deriv_coeff)

        return Polynomial(*der_coeffs)

    def __str__(self):
        terms = []
        for i, coef in enumerate(self.coefficents):
            if coef == 0:
                continue
            if i == 0:
                terms.append(f"{coef}")
            elif i == 1:
                if coef == 1:
                    terms.append("x")
                elif coef == -1:
                    terms.append("-x")
                else:
                    terms.append(f"{coef}x")
            else:
                if coef == 1:
                    terms.append(f"x^{i}")
                elif coef == -1:
                    terms.append(f"-x^{i}")
                else:
                    terms.append(f"{coef}x^{i}")

        result = terms[0]
        for term in terms[1:]:
            if term.startswith('-'):
                result += f" - {term[1:]}"
            else:
                result += f" + {term}"

        return result if terms else "0"