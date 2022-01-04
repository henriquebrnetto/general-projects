# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 15:14:00 2021

@author: Henrique
"""

import pandas as pd
import random

df = pd.read_csv("nba_players_19.csv")
x = random.randint(0,493)
name = f"{df.iloc[x,0]} {df.iloc[x,1]}"
i = 1

while i <=3:
    guess = input("Guess the player: ")
    if guess.lower() == name.lower():
        print("You guessed it!")
        break
    if i == 1:
        print(f"Not this time... But here's a tip\nthe player's team is the {df.iloc[x,2]}")
    if i == 2:
        option = random.choice(["position","number"])
        if option == "position":
            print(f"Not this time... But here's another tip\nthe player's position is {df.iloc[x,4]}")
        if option == "number":
            print(f"Not this time... But here's another tip\nthe player's jersey number is {int(df.iloc[x,5])}")
    if i == 3:
        print(f"You lost. The player was {name}")
    i+=1
        