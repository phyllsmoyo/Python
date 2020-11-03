# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 02:44:34 2020

@author: phyll
"""

import sys

print('Simple calculator')

#First Number
a = input('First number? ')
if a.isnumeric() == False:
    print('Please input a number.')
    sys.exit()

#Operation
operation = input('Operation? ')

#Create a list of recognised operations
operations = ["+", "-", "*", "/", "**", "%"]

#Test if operation input is part of the recognised list
if operation not in operations:
    print('Operation not recognized.')
    sys.exit()

#Second Number
b = input('Second number? ')
if a.isnumeric() == False or b.isnumeric() == False:
    print('Please input a number.')
    sys.exit()
    
#Coonvert input to int
a = int(a)
b = int(b)

#Apply the operator on the input
Sum = 'sum of '+ str(a) + ' + ' + str(b) + ' equals ' + str(a + b)
Difference = 'difference of '+ str(a) + ' - ' + str(b) + ' equals ' + str(a - b)
Product = 'product of '+ str(a) + ' * ' + str(b) + ' equals ' + str(a * b)
Quotient = 'quotient of '+ str(a) + ' / ' + str(b) + ' equals ' + str(a / b)
Exponent = 'exponent of '+ str(a) + ' ** ' + str(b) + ' equals ' + str(a ** b)
Modulus = 'modulus of '+ str(a) + ' % ' + str(b) + ' equals ' + str(a % b)

#Select the combination based on operator    
if operation == "+":
    print(Sum)

elif operation == "-":
    print(Difference)
    
elif operation == "*":
    print(Product)
    
elif operation == "/":
    print (Quotient)
    
elif operation == "**":
    print(Exponent)
    
elif operation == "%":
    print(Modulus)
    