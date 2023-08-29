import random

user_win = 0
comp_win = 0

options = ["rock", "paper", "scissors"]
options[0]

while True:
	user_input = input("Type Rock/Paper/Scissors or q to quit: ").lower()
	if user_input == "q":
		break

	if user_input not in options:
		continue

	random_number = random.randint(0, 2)
	# rock is 0, paper is 1, scissors is 2
	comp_pick = options[random_number]
	print("Computer picked", comp_pick + ".")

	if user_input == "rock" and comp_pick == "scissors":
		print("You won!")
		user_win += 1
	elif user_input == "paper" and comp_pick == "rock":
		print("You won!")
		user_win += 1
	elif user_input == "scissors" and comp_pick == "paper":
		print("You won!")
		user_win += 1
	else: 
		print("You lost!")
		comp_win += 1
	
	
print("You won", user_win, "times.")
print("Comp won", comp_win, "times.")
print("Goodbye!")