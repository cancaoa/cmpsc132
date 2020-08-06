# Cmpsc 132
# Lab 3: Working with Functions
# Omer Canca

import math     # Basic operations
import cmath    # Import cmath in order to insert square root function

def calcMathOperations(s, r):

    # Print results
    print(s, '+', r, '=', s + r)
    print(s, '-', r, '=', s - r)
    print(s, '*', r, '=', s * r)
    print(s, '/', r, '=', s / r)

def calcPythagThm(a, b):


    #Calculate and print the answer
    c = cmath.sqrt((a**2) + (b**2))
    print('c:', c)

def calcQuadForm(a, b, c):
    # Explain what the program does
    print('This program will produce two answers using the quadratic formula based off of user inputs')

    # Create a value for the discriminant
    d = ((b**2) - (4 * a * c))

    # Create a value for the denominator
    e = (2 * a)

   # Check to see if negative values exist under the radical
    if d < 0:
        print('Error. The first solution is undefined. There is a negative in the radical. It will now restart. ')

    # Check to see if there are zeros in the denominator
    if e==0:
        print('Error. The first solution is undefined. There is a 0 in the denominator. It will now restart. ')

    #if there are no errors, solve the equation
    else:

        # Use quadratic formula to have program calculate answers
        # Use an addition formula and a subtraction formula
        solution_1 = (-b + cmath.sqrt(d)) / (e)
        solution_2 = (-b - cmath.sqrt(d)) / (e)

        # Print the solutions for the user
        print('The first solution is ', solution_1)
        print('The second solution is ', solution_2)