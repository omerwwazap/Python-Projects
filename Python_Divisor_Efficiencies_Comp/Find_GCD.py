# find mod of two ints and rutnrn them


def oklid(m, n):
    while n != 0:
        r = m % n
        m = n
        n = r
    return m  #!


m = int(input("enter first positive intgern: "))
n = int(input("enter second positive intgern: "))

gcd = oklid(m, n)
if gcd == 1:
    print("no common divisir")
else:
    print("greatest common divisir is", gcd)
