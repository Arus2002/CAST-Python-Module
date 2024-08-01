from trigonometric import Sin, Cos
from polynomial import Polynomial
import math

if __name__ == "__main__":
    # sin = Sin()
    # cos = Cos()
    # tg = sin/cos
    # print(tg(math.pi/4)) # 1.0
    # tg_ = tg.derivative()
    # print(tg_(math.pi/4)) # 2.0
    # x_2 = Polynomial(0, 0, 1)  # 0*1 + 0*x + 1*x^2
    # print(x_2(12)) # 144
    # sin_2 = x_2.apply(sin)  # sin^2 (x)
    # print(sin_2(3 * math.pi / 2)) # 1.0
    # cos_x_2 = cos.apply(x_2)  # cos(x^2)
    # print(cos_x_2(-math.sqrt(math.pi))) # -1.0
    sin = Sin()
    cos = Cos()
    print(sin(math.pi))
    applied = cos.apply(cos.apply(cos))
    der = applied.derivative() #cos(cosx)*(-sinx)
    print(der(math.pi / 4))
    
