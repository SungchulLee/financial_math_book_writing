import numpy as np

coupon = 0.01
face_value = 100

price = 99 + (21+3/4) / 32
print(price)

#                       price           continuous compounding discrete compounding
# yield_rate = 0.0106 # 99.6796875      99.69491779393837      99.70856275264174
yield_rate = 0.0107   # 99.6796875      99.64618584276408      99.6600821321915
# yield_rate = 0.0108 # 99.6796875      99.59747805070536      99.61162782828589

value_discrete_compounding = 0
value_continuous_compounding = 0
for i in range(1,11):
    period = 0.5 * i
    value_discrete_compounding += face_value*(coupon/2)/(1+yield_rate/2)**i
    value_continuous_compounding += face_value*(coupon/2)*np.exp(-yield_rate*period)
value_discrete_compounding += face_value/(1+yield_rate/2)**i
value_continuous_compounding += face_value*np.exp(-yield_rate*period)
print(value_discrete_compounding)
print(value_continuous_compounding)