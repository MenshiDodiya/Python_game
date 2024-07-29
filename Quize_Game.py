#Computer Quiz game

print("Welcome to my computer quiz!")

playing = input("If you want to play quiz? ")
name = input("What is your name? ")

if playing.lower() != "yes":
    quit()
print("Okay! Let's play :)")
score = 0

answer = input("1) What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("2) What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("3) What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("4) What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("5) What does OS stands for? ")
if answer.lower() == "operating system":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("6) What does HDD stand for? ")
if answer.lower() == "hard disk drive":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("7) What does ROM stand for? ")
if answer.lower() == "read only memory":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("8) What does DVD stand for? ")
if answer.lower() == "digital video disk":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("9) What does HTML stand for? ")
if answer.lower() == "hyper text markup language":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("10) What does PDF stand for? ")
if answer.lower() == "portable document formate":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

print(f"{name} got "+str(score)+" question correct out of 10!")
print("you got "+str((score/10)*100)+"%.")