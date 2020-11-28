# inport packages to extend python (just like we extend subline, or Atom, or VSCode)
from random import randint

# re-import our game variables
from gameComponents import gameVars, winLose

# set up our game loop
while gameVars.player is False:
	print("=====================*/ RPS GAME /*======================")
	print("---------------------------------------------------------")
	print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
	print("gameVars.player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
	print("---------------------------------------------------------")
	print("=========================================================")

	print("Choose your weapon! or type quit to exit\n") #\n means "new line"
	# this is the player choice
	gameVars.player = input("choose rock, paper or scissors: \n")

	# if the player chose to quit, then exit the game
	if gameVars.player == "quit":
		print("you chose to quit, quitter!")
		exit()

	# player = true -> it has a value (rock, paper, or scissors)

	# this will be the AI choice -> a random pick from the choices array
	computer = gameVars.choices[randint(0, 2)]

	# check to see what the user input

	# print outputs whatever is in the round brackets -> in this case it outputs player to the command prompt window
	print("user chose: " + gameVars.player)

	# validate that the random choice worked for the AI
	print("AI chose: " + computer)

	if (computer == gameVars.player):
		print("tie")

	# always check for negative conditions first (the losing case)
	elif(computer == "rock"):
		if(gameVars.player == "scissors"):
			gameVars.player_lives -= 1
			print("you lose! player lives: ", gameVars.player_lives)
		else:
			print("you win!")
			gameVars.computer_lives -= 1

	elif (computer == "paper"):
		if (gameVars.player == "scissors"):
			gameVars.player_lives -= 1
			print("you lose! gameVars.player lives: ", gameVars.player_lives)
		else:
			print("you win!")
			gameVars.computer_lives -= 1

	elif (computer == "scissors"):
		if (gameVars.player == "rock"):
			gameVars.player_lives -= 1
			print("you lose! gameVars.player lives: ", gameVars.player_lives)
		else:
			print("you win!")
			gameVars.computer_lives -= 1
	
	if gameVars.player_lives == 0:
		winLose.winorlose("lost")

	elif gameVars.computer_lives == 0:
		winLose.winorlose("won")

	else:
		gameVars.player = False


	print("gameVars.player has:", gameVars.player_lives, "lives left")
	print("AI has:", gameVars.computer_lives, "Lives left")

	# make the loop keep running by setting gameVars.player back to False
	# unset, so that our loop condition above will evaluate to True
	gameVars.player = False
