# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 16:01:33 2021

@author: Henrique
"""

import random

print("Rock, Paper or Scissor")

player = 0
comp = 0
i = 1

while i <=3:
    if player == 2:
        print("Well played, you won!")
        break
    if comp == 2:
        print("You lost... better luck next time")
        break
    comp_move = random.choice(["rock","paper","scissor"])
    player_move = input("Make your move: ")
    player_move = player_move.lower()
    comp_move = comp_move.lower()
    
    if player_move == comp_move:
        print("Again...")
    if player_move != "rock" and player_move != "paper" and player_move != "scissor":
        print("Again...")
    if player_move == "rock" and comp_move == "paper":
        print("You lost\n")
        comp += 1
        print(f"player: {player}  ||  computer: {comp}")
        
    if player_move == "rock" and comp_move == "scissor":
        print("You won!")
        player += 1
        print(f"player: {player}  ||  computer: {comp}")  
        
    if player_move == "paper" and comp_move == "rock":
        print("You won!")
        player += 1
        print(f"player: {player}  ||  computer: {comp}")  
        
    if player_move == "paper" and comp_move == "scissor":
        print("You lost\n")
        comp += 1
        print(f"player: {player}  ||  computer: {comp}")
        
    if player_move == "scissor" and comp_move == "rock":
        print("You lost\n")
        comp += 1
        print(f"player: {player}  ||  computer: {comp}")
        
    if player_move == "scissor" and comp_move == "paper":
        print("You won!")
        player += 1
        print(f"player: {player}  ||  computer: {comp}")  