#a. Write a function that takes two positive integer and returns GCD which is found by
#Consecutive Integer Checking Algorithm.

#b. Using your function write a program that prompts the user to enter two positive integer
#and displays the GCD of them.

#Sample Run:
#Non-negative first integer >=2 please: 64
#Non-negative first integer >=2 please: 12
#greatest common divisor: 4

import time
start = time.clock()

#=========================================
def gcd(number1, number2):
    if number2 == 0:
        return number1
    return gcd(number2, number1%number2)
#=========================================
number1=int(input('Non-negative first integer >=2): '))
number2=int(input('Non-negative first integer >=2): '))
answer=gcd(number1,number2)

print('greatest common divisor: ',answer)

end = time.clock()
print(end - start)

    
