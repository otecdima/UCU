import math
x = float(input(''))

COS = math.cosh(x)
print ('COS =' f'{COS: .4f}')

EXP = 0.5*(math.exp(x) + math.exp(-x))
print('EXP =' f'{EXP: .4f}')

E = 0.5 * (math.e ** x + math.e ** -x)

print('E =' f'{E: .4f}')


