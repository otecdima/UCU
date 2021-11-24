lst = [1,2,3,4,5,6,7,8]

def reverse(lst, n=0):
    if n >= len(lst)/2:
        return lst
    else:
        lst[n], lst[-1-n] = lst[-1-n], lst[n]
        return reverse(lst, n+1)
print(reverse(lst, 0))