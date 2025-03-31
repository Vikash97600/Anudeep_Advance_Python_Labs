# 1● Imagine you are developing a personal finance tracking application. 
# Create a custom module named finance.py that includes functions for calculating expenses, income, and savings.
# Describe the functions you would include and how you would import this module in your main application.

from finance import *

if __name__== "__main__":
    expenses=[1500,200,300]
    incomes=[4000.1500]
    total_expenses = calculate_expenses(expenses)                    #2000
    total_income = calculate_income(incomes)                         #5500
    total_savings = calculate_savings(total_income, total_expenses)  #3500

    print(f"Total Expenses: ${total_expenses}")
    print(f"Total Income: ${total_income}")
    print(f"Total Savings: ${total_savings}")



# 2: ● Import the random module as rnd and generate a random integer between 1 and 100. 
# ● Import the math module and calculate the square root of 49 and the sine of 90 degrees (convert degrees to radians using math.radians).

import random as rnd
import math

randomNumber = rnd.randint(1, 100)

num=49
square_root = math.sqrt(num)

sineValue = math.sin(math.radians(90))

print(f"The Random number between 1 and 100: {randomNumber}")
print(f"The Square root of the number {num} is: {square_root}")
print(f"The Sine of 90 degrees is : {sineValue}")