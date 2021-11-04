import math
mass = float(input())
speed = float(input())
c = 299792458

massr = mass // math.sqrt(1-((speed**2)//(c**2)))
E = massr * c **2
print (E)

