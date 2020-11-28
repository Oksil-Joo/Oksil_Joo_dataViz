# inport packages to extend python (just like we extend subline, or Atom, or VSCode)
from random import randint

# [] => this is an array. an array is a special type of container that can hold multipe itmes
# arrays are indexed (their contents get assigned a number)
# The index alwyas starts at 0
choices = ["rock", "paper", "scissors"]


player_lives = 1
AI_lives = 1

total_lives = 1

player = False;

# define a win or lose funtion
def winorlose(status):
	# print("inside winorlose function; status is: ", status)

	#print("You", status, "! Would you like to play again?")
	#choice = input("Y / N? ")
	if status == "won":
		pre_message = "You are the Yuuuuuuuuuugest winner ever! "
	else:
		pre_message = "You done trumped it, loser! "
	
	print(pre_message + "Would you like to play again? ")
	
	choice = input("Y / N? ")

	if choice == "Y" or choice == "y":
		
		global player_lives
		global AI_lives
		global player

		player_lives = 1
		AI_lives = 1
		player = False

	
	elif choice == "N" or choice == "n":
		# exit messae and quit
		print("You choose to quit! Better luck next time!")
		exit()

	else:
		print("Make a valid choice - Y or N")
		#this will generate a bug that we need to fix later
		choice = input("Y / N: ")

# set up our game loop
while player is False:
	print("=====================*/ RPS GAME /*======================")
	print("Computer Lives:", AI_lives, "/", total_lives)
	print("player Lives:", player_lives, "/", total_lives)
	print("=========================================================")

	print("Choose your weapon! or type quit to exit\n") #\n means "new line"
	# this is the player choice
	player = input("choose rock, paper or scissors: \n")

	# if the player chose to quit, then exit the game
	if player == "quit":
		print("you chose to quit, quitter!")
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
			player_lives = player_lives - 1
			print("you lose! player lives: ", player_lives)
		else:
			print("you win!")
			AI_lives = AI_lives - 1

	elif (computer == "paper"):
		if (player == "scissors"):
			player_lives = player_lives - 1
			print("you lose! player lives: ", player_lives)
		else:
			print("you win!")
			AI_lives = AI_lives - 1

	elif (computer == "scissors"):
		if (player == "rock"):
			player_lives = player_lives - 1
			print("you lose! player lives: ", player_lives)
		else:
			print("you win!")
			AI_lives = AI_lives - 1
	
	if player_lives == 0:
		winorlose("lost")

		

	elif AI_lives == 0:
		winorlose("won")

	else:
		player = False


	print("player has:", player_lives, "lives left")
	print("AI has:", AI_lives, "Lives left")

	# make the loop keep running by setting player back to False
	# unset, so that our loop condition above will evaluate to True
	player = False
