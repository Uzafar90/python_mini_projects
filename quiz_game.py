print("Welcome to my computer quiz!")

playing = input("Do you want to play the game? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play the game!!!")
score = 0
points = (score / 10) * 100

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit" :
    print('Correct answer')
    score += 1
else: 
    print("Incorrect answer")

answer = input("What does RAM stand for? ")
if answer.lower() == "Random Access Memory":
    print('Correct answer')
    score += 1
else: 
    print("Incorrect answer")
answer = input("What does GPU stand for? ")
if answer.lower() == "Graphic Processing Unit":
    print('Correct answer')
    score += 1
else: 
    print("Incorrect answer")
answer = input("What does HDD stand for? ")
if answer.lower() == "Hard Disk Drive":
    print('Correct answer')
    score += 1
else: 
    print("Incorrect answer")
answer = input("What does SSD stand for? ")
if answer.lower() == "Solid State Drive":
    print('Correct answer')
    score += 1
else: 
    print("Incorrect answer")
answer = input("What does USB stand for? ")
if answer.lower() == "Universal Serial Bus":
    print('Correct answer')
    score += 1
else: 
    print("Incorrect answer")
answer = input("What does LAN stand for? ")
if answer.lower() == "Local Area Network":
    print('Correct answer')
    score += 1
else: 
    print("Incorrect answer")
answer = input("What does WAN stand for? ")
if answer.lower() == "Wide Area Network":
    print('Correct answer')
    score += 1
else: 
    print("Incorrect answer")
answer = input("What does BIOS stand for? ")
if answer.lower() == "Basic Input/Output System":
    print('Correct answer')
    score += 1
else: 
    print("Incorrect answer")
answer = input("What does OS stand for? ")
if answer.lower() == "Operating System":
    print('Correct answer')
    score += 1
else: 
    print("Incorrect answer")



print(f"You got {score} points and {points}%")