# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 02:24:38 2020

@author: phyll
"""
from sys import exit


fahrenheit = input("What is the temperature in fahrenheit?")

if fahrenheit.isnumeric() == False:
    print("Input is not a number.")

    exit()

else:
    celcius = int((int(fahrenheit) - 32) * 5 / 9)

print("Temperature in Celcius is {}".format(celcius))
