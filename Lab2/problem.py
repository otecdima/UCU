import math
r = float(input())
h = float(input())
V = h * math.pi * r ** 2
A = h * 2 * math.pi * r + 2 * math.pi * r ** 2

if V == 0.000:
    print ("V =", f'{V: .1f}')
else: 
    print ("V =", f'{V: .3f}')

if A == 0.000:
    print ("A =", f'{A: .1f}')
else:
    print ("A =", f'{A: .3f}')