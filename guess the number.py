# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 14:16:44 2021

@author: Henrique
"""

import random

x = random.randint(0,100)
i = 1

while i <= 5:
    guessed_num = int(input("Guess a number between 0 and 100... "))
    while type(guessed_num) != int:
        guessed_num = input("You did not input a valid number... ")
    while guessed_num < 0 and guessed_num > 100:
        guessed_num = input("Please insert a number between 0 and 100... ")
    diff = abs(guessed_num - x)
    def approx(i):
        if i == 1:
            a = random.randint(9,10)
        if i == 2:
            a = random.randint(7,8)
        if i == 3:
            a = random.randint(5,6)
        if i == 4:
            a = random.randint(3,4)
        if i == 5:
            a = random.randint(1,2)
        return a
    if i == 5:
        print("Close, but not quite...")
        print(f"You were almost there... the answer was {x}")
        break
    if guessed_num == x:
        print("Good one ;)")
        break
    else:
        print(f"Your number is at most ±{diff + approx(i)} from the right one")
    i+=1