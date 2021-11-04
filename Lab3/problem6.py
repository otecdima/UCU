number = int(input())

if number > 3:
    print("*")
    print("**")
    for i in range(3, number):
        print("*" + " "*(i-2) + "*")
    for i in range (number, number+1):
        print("*"*i)
else:
    for i in range(1, number+1):
        print("*"*i)
    
        


