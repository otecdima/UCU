codegray = input()
number = []
number.append(codegray[0])

for i in range (1, len(codegray)):
    number.append(str(int(codegray[i]) ^ int(number[i-1])))
number = ''.join(number)
print(number)
