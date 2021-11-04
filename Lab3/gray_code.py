num = input()
number = int("0b" + num, base = 2)
g = 0
g = number ^ (number >> 1)
print (bin(g)[2:].zfill(len(num)))