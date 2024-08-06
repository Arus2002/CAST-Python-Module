from trigonometric import Sin, Cos
from polynomial import Polynomial
import math

if __name__ == "__main__":
    # Test 1
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

    # Test 2
    # sin = Sin()
    # print(sin)
    # cos = Cos()
    # print(cos)
    # complex_func = cos.apply(cos.apply(cos)).derivative()
    # print(complex_func)
    # print(complex_func(math.pi / 2))

    # Test 3
    # sin = Sin()
    # cos = Cos()
    # print((cos.apply(cos.apply(cos))).derivative()(math.pi / 2))
    # print((cos.apply(cos.apply(cos)))(math.pi / 2))

    # Test 4
    sin = Sin()
    cos = Cos()
    x_2 = Polynomial(0, -1, 1)  # 0*1 + 0*x + 1*x^2
    complex = (cos.apply(cos.apply(x_2))).derivative()
    print(complex)
    print((cos.apply(cos.apply(x_2)))(math.pi / 2))