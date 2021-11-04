x, y = input("Enter two values: ").split()
x = int(x)
y = int(y)
hemmingnumber = 0
distance = x ^ y

for i in range (distance.bit_length()):
    if distance & 1:
        hemmingnumber = hemmingnumber + 1
    distance = distance >> 1

print(hemmingnumber)


    
    
    
    
    