#!/bin/python3

from BudgetApp import Shoes

low = Shoes('And 1s', 30)
medium = Shoes('Air Force 1s',120)
high = Shoes('off whites',400)

try :
    shoe_budget = float(input('What is your shoe budget? '))
except ValueError:
    exit('Please enter a number')

for shoes in [high,medium,low]:
    shoes.buy(shoe_budget)