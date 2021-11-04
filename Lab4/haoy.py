def happy(n):
    while n!=1:
        n=str(n)
        j=0
        for dig in n:
            j+=(int(dig))**2
            n=j
        if n==4:
            return False
    return True
print(happy(32))
print(happy(33))