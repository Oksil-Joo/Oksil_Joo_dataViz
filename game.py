# inport packages to extend python (just like we extend subline, or Atom, or VSCode)
from random import randint

# [] => this is an array. an array is a special type of container that can hold multipe itmes
# arrays are indexed (their contents get assigned a number)
# The index alwyas starts at 0
choices = ["rock", "paper", "scissors"]


player_lives = 1
AI_lives = 1

total_lives = 1

# this is the player choice
# player = input("choose rock, paper or scissors: ")

# True and false are Boolean data types -> they are the equivalent of on or off, 1 or 0
player = False

while player is False:
	print("=====================*/ RPS GAME /*======================")
	print("computer Lives:", AI_lives, "/", total_lives)
	print("player Lives:", player_lives, "/", total_lives)
	print("=========================================================")

	print("Choose your weapon! or type quit to exit\n") #\n means "new line"
	# this is the player choice
	player = input("choose rock, paper or scissors: \n")

	# if the player chose to quit, then exit the game
	if player == "quit":
		print("you chose to quit")
		exit()

	# player = true -> it has a value (rock, paper, or scissors)

	# this will be the AI choice -> a random pick from the choices array
	computer = choices[randint(0, 2)]

	# check to see what the user input

	# print outputs whatever is in the round brackets -> in this case it outputs player to the command prompt window
	print("user chose: " + player)

	# validate that the random choice worked for the AI
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
		if (player == "rock"):
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
	
	if player_lives == 0:
		print("You lose! Would you like to play again?")
		choice = input("Y / N? ")

		if choice == "N" or choice == "n":
			print("You chose to quit! Better luck next time!")
			exit()

		elif choice == "Y" or choice == "y":
			# reset the player lives and the AI Lives
			# and set player to False so that our loop will restart
			player_lives = 1
			AI_lives = 1
			player = False

		else:
			print("Make a valid choice - Y or N")
			#this will generate a bug that we need to fix later
			choice = input("Y / N: ")

	if AI_lives == 0:
		print("You won! Would you like to play again?")
		choice = input("Y / N? ")

		if choice == "N" or choice == "n":
			print("You choose to quit! Better luck next time!")
			exit()

		elif choice == "Y" or choice == "y":
			# reset the player lives and the AI Lives
			# and set player to False so that our loop will restart
			player_lives = 1
			AI_lives = 1
			player = False

		else:
			print("Make a valid choice - Y or N")
			#this will generate a bug that we need to fix later
			choice = input("Y / N: ")


	print("player has:", player_lives, "lives left")
	print("AI has:", AI_lives, "Lives left")

	# make the loop keep running by setting player back to False
	# unset, so that our loop condition above will evaluate to True
	player = False
