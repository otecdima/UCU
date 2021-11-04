import math

x = float(input())
y = float(input())
o = float(input())

l = (1 / math.sqrt(2*math.pi*o**2)) * math.e ** ((-1) * (((x-y)**2)/(2*o**2)))

print(f'{l: .10f}')