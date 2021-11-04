import math


def sales_prediction():
    allsales = float(input())
    annualincome = allsales * 1.19
    print(annualincome)
    pass


def yard_to_meter():
    lengthinyards = float(input())
    linmm = lengthinyards * 914
    linm = lengthinyards * 0.914
    linkm = lengthinyards * 0.000914
    print (linmm)
    print (linm)
    print (linkm)
    pass


def cashier():
    goods1 = float(input())
    goods2 = float(input())
    goods3 = float(input())
    goods4 = float(input())
    goods5 = float(input())
    sum = goods1 + goods2 + goods3 + goods4 + goods5
    print (sum)
    pdv = 0.14 * sum
    print (pdv)
    generalsum = sum + pdv
    print (pdv)
    pass


def odometer():
    v0 = float(input())
    a = float(input())
    t1 = float(input())
    t2 = float(input())
    v = v0 + a * t1
    Swithacceleration = abs(v * t2 + (a * t1 ** 2)/2)
    Swithoutacceleration = abs(v * t2)
    print (Swithacceleration)
    pass



def payment_instalments():
    sum = float(input())
    numerosity = int(input())
    finalsum = sum + 0.05*sum
    everypay = finalsum/numerosity
    print (finalsum)
    print (everypay)
    pass


def miles_per_galon():
    miles = float(input())
    usedfuel = float(input())
    MPG = miles/usedfuel
    print (MPG)
    pass


def cookie():
    cookies = int(input())
    numerosity = 48
    sugar = 1.5 * (cookies/numerosity)
    butter = 1 * (cookies/numerosity)
    flour = 2.75 *(cookies/numerosity)
    print (sugar)
    print (butter)
    print (flour)
    pass


def vineyard():
    R = float(input())
    E = float(input())
    S = float(input())
    V = math.trunc((R - 2*E)/S)
    print (V) 
    pass


def compound_interest():
    P = float(input())
    r = float(input())
    n = int(input())
    t = float(input())
    A = P * (1+((r/100)/n))**(n*t)
    print (A)
    pass


if __name__ == "__main__":
    eval(input() + "()")
