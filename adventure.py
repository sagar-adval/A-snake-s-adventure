import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0
body = []

wn = turtle.Screen()
wn.title("A Snake's Adventure")
wn.bgcolor("black")
wn.setup(width=1200, height=720)
wn.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("blue")
head.penup()
head.goto(0, 0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
count1 = 0
food.shape("circle")
food.color(random.choice(["blue", "orange", "yellow", "purple", "green"]))
food.penup()
food.goto(random.randint(-580, 580), random.randint(-340, 340))

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center")


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)



wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")


while True:
    wn.update()

    if head.xcor() > 600 or head.xcor() < -600 or head.ycor() > 360 or head.ycor() < -360:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for segment in body:
            segment.goto(1000, 1000)

        body.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center")

    if head.distance(food) < 15:

        x = random.randint(-590, 590)
        y = random.randint(-350, 350)
        food.goto(x, y)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        food.color(random.choice(["blue", "orange", "yellow", "purple", "green"]))
        new_segment.color(random.choice(["blue", "orange", "yellow", "purple", "green"]))
        new_segment.penup()
        body.append(new_segment)
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center")

    for index in range(len(body) - 1, 0, -1):
        x = body[index - 1].xcor()
        y = body[index - 1].ycor()
        body[index].goto(x, y)

    if len(body) > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x, y)

    move()
    time.sleep(0.1)

wn.mainloop()