from turtle import Turtle, Screen
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
segments = []
positions = [(0, 0), (-20, 0), (-40, 0)]

for pos in positions:
    seg = Turtle("square")
    seg.color("white")
    seg.penup()
    seg.goto(pos)
    segments.append(seg)

head = segments[0]

food = Turtle("circle")
food.color("red")
food.penup()
food.shapesize(0.5, 0.5)
food.speed("fastest")
food.goto(random.randint(-280, 280), random.randint(-280, 280))

score = 0
scoreboard = Turtle()
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write(f"Score: {score}", align="center", font=("Arial", 18, "normal"))

def up():
    if head.heading() != 270:
        head.setheading(90)

def down():
    if head.heading() != 90:
        head.setheading(270)

def left():
    if head.heading() != 0:
        head.setheading(180)

def right():
    if head.heading() != 180:
        head.setheading(0)

screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    for i in range(len(segments) - 1, 0, -1):
        segments[i].goto(segments[i - 1].pos())
    head.forward(20)

    if (
        head.xcor() > 290 or head.xcor() < -290 or
        head.ycor() > 290 or head.ycor() < -290
    ):
        game_on = False
        scoreboard.goto(0, 0)
        scoreboard.write("GAME OVER 💀", align="center", font=("Arial", 24, "bold"))

    if head.distance(food) < 15:
        food.goto(random.randint(-280, 280), random.randint(-280, 280))

        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        segments.append(new_seg)

        score += 1
        scoreboard.clear()
        scoreboard.goto(0, 260)
        scoreboard.write(f"Score: {score}", align="center", font=("Arial", 18, "normal"))

screen.exitonclick()
