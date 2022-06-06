# -*- coding: utf-8 -*-
"""
program to calculate the sum of any parsed factorial’s digits
"""
import math 

sum_of_digits = 0
num = int(input("Enter a numerical integer: "))

fac = math.factorial(num)

for digit in str(fac):

  sum_of_digits += int(digit)

print(sum_of_digits)

