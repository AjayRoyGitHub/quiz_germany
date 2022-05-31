# Quiz Game

print("Welcome to a Small Quiz game about Germany")
playing = input("Do you want to play the Game (yes/no)? ")
if playing.lower() != "yes":
    quit()
print("Okay! Let's Play!!!")
score = 0
answer = input("What is the Capital of Germany? ")
if answer.lower() == "berlin":
    print("Great,You are correct")
    score += 1
else:
    print("Sorry, You are Wrong!!!")
answer = input("Who is the Chancellor of Germany (2022)? ")
if answer.lower() == "olaf scholz":
    print("Great,You are correct")
    score += 1
else:
    print("Sorry, You are Wrong!!!")
answer = int(input("How many countries are part of European Union? "))
if answer == 27:
    print("Great,You are correct")
    score += 1
else:
    print("Sorry, You are Wrong!!!")
answer = input("What is the currency of Germany? ")
if answer.lower() == "euro":
    print("Great,You are correct")
    score += 1
else:
    print("Sorry, You are Wrong!!!")
answer = int(input("How many Federal States are there in Germany? "))
if answer == 16:
    print("Great,You are correct")
    score += 1
else:
    print("Sorry,You are Wrong!!!")
print("Your final score is" + str(score) + "points")
print("You are " + str((score/5)*100) + "% correct")
print("Thanks for playing....Bye")
