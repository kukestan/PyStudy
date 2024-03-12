from mpmath import mp  
  
# 设置精度为1000位  
mp.dps = 1000
  
# 计算π的值  
pi_value = mp.pi  
  
# 显示π的前1000位  
print(str(pi_value)[:1001])  # 使用切片来确保只获取前1000位数字和一个小数点
#print(pi_value)