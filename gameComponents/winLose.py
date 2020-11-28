from gameComponents import gameVars

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
		
		gameVars.player_lives = 1
		gameVars.computer_lives = 1
		gameVars.player = False

	
	elif choice == "N" or choice == "n":
		# exit messae and quit
		print("You choose to quit! Better luck next time!")
		exit()

	else:
		print("Make a valid choice - Y or N")
		#this will generate a bug that we need to fix later
		choice = input("Y / N: ")