#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import time
import decimal
# objective is a random dollar amount is generated as a price, to which you insert a dollar amount for the payment...
# ... to which you get your change back in quarters, dimes, nickles, and pennies.
random.randint(0, 10000)/100

penny = decimal.Decimal(.01)
nickle = decimal.Decimal(.05)
dime = decimal.Decimal(.10)

ttlpenny = 1
ttlnickle = 0
ttldime = 0
ttlquarter = 0
price = random.randint(0, 1000)/100
price = decimal.Decimal(price)
price = round(price, 2)


quarter = decimal.Decimal(.25)

def func1(price):
   
    print(f'You owe: {price}')
    user_input = decimal.Decimal(input('Enter payment now:'))
    if user_input < price:
        print('Invalid input')
        func1(price)
    print(f'You inserted: {user_input}')
    change = user_input - price
    change = decimal.Decimal(change)
    print(f'Your change is: {change}')
    change1(change, ttlquarter, ttldime, ttlnickle, ttlpenny)

def change1(change, ttlquarter, ttldime, ttlnickle, ttlpenny):
    if change > 0:
        if change >= quarter:
            change = change - quarter
            ttlquarter = ttlquarter +1
            change1(change, ttlquarter, ttldime, ttlnickle, ttlpenny)
        if change >= dime:
            change = change - dime
            ttldime = ttldime +1
            change1(change, ttlquarter, ttldime, ttlnickle, ttlpenny)
        
        if change >= nickle:
            change = change - nickle
            ttlnickle = ttlnickle +1
            change1(change, ttlquarter, ttldime, ttlnickle, ttlpenny)
        
        if change >= penny:
            change = change - penny
            ttlpenny = ttlpenny +1
            change1(change, ttlquarter, ttldime, ttlnickle, ttlpenny)
        if change <= .01: 
            print(f'You are given: {ttlquarter} quarters, {ttldime} dimes, {ttlnickle} nickles, and {ttlpenny} pennies')
            new()

def new():
    print('Would you like to make another purchase?')
    user_input = input('press enter to continue')
    func1(price)
    
func1(price)

