# Write a function that takes an integer, n, as a parameter and displays a n-by-n matrix.
# Each element in the matrix is 0 or 1, which is generated randomly.

# Hint: You can generate a random integer number between x and y (inclusive) by
# using the function random.randint(x, y).
# import random library fort his function as the first statement in your program.

# b. Using your function write a program that prompts the user to enter a positive integer n
# and displays an n-by-n matrix.

# Sample run:
# Enter a positive integer: 6
# 0 0 1 1 1 1
# 1 1 1 0 1 1
# 0 1 1 0 1 0
# 0 1 1 0 1 1
# 1 1 1 0 1 0
# 1 1 0 1 1 0

import random

my_number = int(input("Enter an positve integer"))

for row in range(my_number):
    for col in range(my_number):
        print(" %3d" % random.randint(0, 1), end="")
    print()
