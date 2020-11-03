# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 01:49:53 2020

@author: phyll
"""

# =============================================================================
# numeric_value = '7.1'
# print(numeric_value.isdecimal())
# 
# string_value = 'Bob'
# print(string_value.isalpha())
# =============================================================================

first_value = input('First Number: ')
second_value = input('Second Number: ')

if first_value.isnumeric() == False or second_value.isnumeric() == False:
    print ('Values is not a number. Please enter numbers only')
    exit()
    
    
first_value = int(first_value)
second_value = int(second_value)

sum = first_value + second_value
print('Sum: {}'.format(sum))

