from sympy import symbols, Add, Mul, solve, Eq, diff, integrate, simplify, expand, Matrix 
#定义符号
x, y = symbols('x y')

#基本运算
expr = Add(x, y)  # x + y 
print(expr)
print(isinstance(expr, Add))
expr = Mul(x, y)  # x * y
print(expr)
print(isinstance(expr, Mul))
expr += 1
print(expr)

#代数运算 
equation = Eq(x**2, 1)  
solutions = solve(equation, x, dict=True)  
print(solutions)  # 输出 [{x: -1}, {x: 1}]

#微积分
diff_expr = diff(x**2, x)  # 求导  
print(diff_expr)  # 输出 2*x  
  
integrate_expr = integrate(x**2, x)  # 积分  
print(integrate_expr)  # 输出 x**3/3

#化简与展开
expr = (x + 1)**2  
expanded_expr = expand(expr)  # 展开  
simplified_expr = simplify(expanded_expr)  # 化简

#矩阵运算
M = Matrix([[1, 2], [3, 4]])  
print(M.T)  # 输出矩阵的转置  
print(M.inv())  # 输出矩阵的逆（如果可逆的话）
 
#解方程
eq1 = Eq(x + y, 1)  
eq2 = Eq(x - y, 3)  
solutions = solve((eq1, eq2), (x, y), dict=True)  
print(solutions)  # 输出 [{x: 2, y: -1}]