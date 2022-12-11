import numpy as np

#Write a program that prints each item in a numerical array individually
a = np.array([1,2,3,4])

def print_lst(num):
    for numbers in num:
        print(numbers)

print_lst(a)