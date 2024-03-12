from math import factorial, sin, cos, tan, radians, gcd, pi, e, inf, log, log2, log10, exp, pow, sqrt, modf

#计算阶乘
print(factorial(4))

#计算三角函数
# 将角度转换为弧度  
angle_in_degrees = 45  
angle_in_radians = radians(angle_in_degrees)
print(sin(angle_in_radians))
print(cos(angle_in_radians))
print(tan(angle_in_radians))

#最大公约数
print(gcd(10, 5))

#最小公倍数
def lcm(a, b):  
    return abs(a * b) // gcd(a, b)
print(lcm(12, 4)) 

#PI
print(pi)

#e
print(e)

#无穷大
print(inf)

#自然对数
print(log10(100))
print(log2(8))
print(log(100, 10))

#幂运算
print(exp(1))
print(sqrt(2))
print(pow(2, 10))

#返回小数部分和整数部分，作为元组 (frac, int)
print(modf(7.6))




