from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(1000,800)
bet=screen.textinput("bet","who will win the race?")
y_positions=[-150,-100,-50,0,50,100,150]
colours = ["red","green","violet","indigo","blue","orange","yellow"]
race=False
li=[]
for i in range(7):
    t=Turtle()
    t.color(colours[i])
    t.penup()
    t.goto(-400,y_positions[i])
    li.append(t)
if bet:
    race=True
while(race):
    for i in li:
        i.forward(random.choice([20,11,12,30,14,10,25,12,30]))
        i.speed(10)
        if i.xcor()>500:
            winner=i.pencolor()
            race=0
if winner==bet:
    print('you won the bet')
else:
    print("you lost the game and the winner is ",winner)


Screen().exitonclick()