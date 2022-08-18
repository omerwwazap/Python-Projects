# a. Write a function, Sieve of Eratosthenes as defined in chapter 1 (CH01 in lecture notes)
# by using python. Do not forget that mathematicians do not consider 1 to be a prime
# number. So output of this function should not include 1. Also, in order to able to use the
# output array of this function in the prime factorization function defined in the 2 nd part
# of the question, you have to eliminate all zero (0) values from output array.

# Hint: you may import math library and you may use math.sqrt(x) and math.floor(x)
# functions in python.

# b. Write a function, prime factorization which will find and return all the prime factors of a
# given positive integer number. This function should call and use the output of Sieve of
# Eratosthenes function while finding prime factorization of the given number.

# c. Write the main program which finds and prints two different positive integers ( let’s say
# m & n) greatest common divisor by using middle school procedure as below..
# Middle-school procedure
# Step 1 Find the prime factorization of m
# Step 2 Find the prime factorization of n
# Step 3 Find all the common prime factors of this two numbers and print them.
# Step 4 Compute the product of all the common prime factors
# and print it as gcd(m,n)

# Sample Run:
# Non-negative integer >=2 please: 64
# Another Non-negative integer >=2 please: 12
# Common prime factors are: [2, 2]
# Greatest common divisor: 4
import time

start = time.clock()
# =========================================
def factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i != 0:
            i += 1
        else:
            n = n / i
            factors.append(i)
    if n > 1:  # for non divisable like 3, 5, 7
        factors.append(n)
    return factors


# =========================================
def gcd(number1, number2):
    if number2 == 0:
        return number1
    return gcd(number2, number1 % number2)


# =========================================
def commonfactorfinder(primelist1, primelist2):
    commonfactor = []
    ans = []
    for item in primelist1:
        for item1 in primelist2:
            if item == item1:
                commonfactor.append(item)
    ans = list(dict.fromkeys(commonfactor))
    return ans


# =========================================
number1 = int(input("Non-negative first integer >=2): "))
number2 = int(input("Non-negative first integer >=2): "))
answer = gcd(number1, number2)
print("greatest common divisor: ", answer)
primelist1 = factors(number1)
primelist2 = factors(number2)
print("First numbers prime factor", primelist1)
print("Second numbers prime factor", primelist2)

print("Common divisors are ", commonfactorfinder(primelist1, primelist2))

end = time.clock()
print(end - start)
