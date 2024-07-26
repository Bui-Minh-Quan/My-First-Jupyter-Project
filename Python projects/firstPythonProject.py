print("Welcome to Quiz game 2024")
playing = input("Do you want to play(y or n): ")

if playing.lower() != "y": quit()

print("Okay! Let's play :) ")

point = 0

answer = input("What do mathematicians call less than zero? ").lower()
if answer == "negative numbers": 
    print("Correct!")
    point += 1
else:
    print("Incorrect! The answer is negative numbers")

answer = input("What the general method to calculate the area of irregular shapes? ").lower()
if answer == "calculus": 
    print("Correct!")
    point += 1
else: 
    print("Incorrect! The answer is calculus")

answer = input("What is the color of the sun? ").lower()
if answer == "white":
    print("Correct!")
    point += 1
else:
    print("Incorrect! The answer is white")


print("You score", point, "out of 3! Congratulations")




