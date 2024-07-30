import turtle
import time
import random

WIDTH, HEIGHT = 500, 550
COLORS = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown",
           "black", "gray", "cyan", "magenta", "lime", "teal", 
           "navy", "maroon", "olive", "silver", "gold"]

def set_turtles(colors):
    turtles = []
    number_of_racers = len(colors)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-(WIDTH / 2) + (WIDTH / (number_of_racers + 1)) * (i + 1), -250)
        turtles.append(racer)
    return turtles

def race(colors):
    turtles = set_turtles(colors)
    isOver = False
    while True:
        for racer in turtles:
            distance = random.randint(1, 20)
            racer.forward(distance)
            x, y = racer.pos()
            if y >= HEIGHT / 2:
                return racer.color()[0]

            
    
def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers(2 - 10): ")
        if racers.isdigit() == False:
            print("Input must be numeric.... Please try again!")
            continue
        racers = int(racers)
        if 2 <= racers <= 10:
            return racers
        print("The number of racers must between 2 and 10") 
            
def initialize_turtle_screen(): 
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle racing!!!")

    return screen

def declare_winner(winner_color):
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.pendown()
    pen.goto(0, 0)
    pen.write(f"{winner_color} turtle win the race", 
              align="center", font=("Arial", 16, "normal"))


screen = initialize_turtle_screen()

racers = screen.textinput("Input", "Please enter the number of racers: ")
while not racers.isdigit() or not 2 <= int(racers) <= 10:
    racers = screen.textinput("Input", "Invalid input. Enter a number between 2 and 10") 

racers = int(racers)

random.shuffle(COLORS)
colors = COLORS[: racers]
winner_color = race(colors)

declare_winner(winner_color)

screen.mainloop()





