import random

while True:
	secret_number = random.randint(1, 100)

	while True:
		guess = int(input("Enter your guess "))
		
		if guess == secret_number:
			print("Congradulations; You guessed the number.")
			break
		elif guess < secret_number:
			print("Try a higher number.")
		else:
			print("Try a lower number.")

	play_again = input("Do you want to play again? (yes/no): ")
	if play_again.lower() != 'yes':
		print("Thanks for playing!")
		break
	
