# inport packages to extend python (just like we extend subline, or Atom, or VSCode)
from random import randint

# [] => this is an array. an array is a special type of container that can hold multipe itmes
# arrays are indexed (their contents get assigned a number)
# The index alwyas starts at 0
choices = ["rock", "paper", "scissors"]

player_lives = 5
AI_lives = 5

total_lives = 5

#this is the player choice
player = input("choose rock, paper or scissors: ")

# this will be the AI choice -> a random pick from the choices array
computer = choices[randint(0, 2)]

# check to see what the user input

#print outputs whatever is in the round brackets -> in this case it outputs player to the command prompt window
print("user chose: " + player)

#validate that the random choice worked for the AI
print("AI chose: " + computer)

if (computer == player):
	print("tie")

# always check for negative conditions first (the losing case)
elif(computer == "rock"):
	if(player == "scissors"):
		print("you lose!")
		player_lives -= 1
	else:
		print("you win!")
		AI_lives -= 1

elif (computer == "paper"):
	if (player == "scissors"):
		print("you lose!")
		player_lives -= 1
	else:
		print("you win!")
		AI_lives -= 1

elif (computer == "scissors"):
	if (player == "paper"):
		print("you lose!")
		player_lives -= 1
	else:
		print("you win")
		AI_lives -= 1
print("player lives:", player_lives)
print("AI lives:", AI_lives)

