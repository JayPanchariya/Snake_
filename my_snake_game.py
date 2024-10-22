import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from insect import Insect

#set up for game
width_wn=700
height_wn= 700
sleep_speed = 0.1
game_is_on = True



wn = turtle.Screen()
wn.title("Snake game @ Jay")
wn.bgcolor("yellow")
wn.setup(width=width_wn, height=height_wn)
wn.tracer(0)        #Turns off the wn updates

serpent = Snake()
food = Food(width_wn, height_wn)
scoreboard = Scoreboard()
insect=Insect(width_wn, height_wn)
wn.listen()

wn.onkey(serpent.up, "Up")
wn.onkey(serpent.down, "Down")
wn.onkey(serpent.left, "Left")
wn.onkey(serpent.right, "Right")
# wn.onkeypress(stop,'g')

while game_is_on:
    wn.update()
    time.sleep(sleep_speed)
    serpent.move()
    if serpent.segments[0].distance(food) < 20:
        food.refresh()
        serpent.extend()
        scoreboard.increase_score(10)
    
    if serpent.segments[0].distance(insect) < 20:
        insect.refresh()
        serpent.extend()
        scoreboard.increase_score(20)    
    
    if serpent.segments[0].xcor() > ((width_wn//2)-20) or serpent.segments[0].xcor() < -((width_wn//2)-20) or serpent.segments[0].ycor() > ((height_wn//2)-20) or serpent.segments[0].ycor() < -((height_wn//2)-20):
        # game_is_on = False
        # scoreboard.game_over()
        for segment in serpent.segments:
            segment.goto(1000,1000)
        serpent.reset()
        scoreboard.reset()
        time.sleep(2)
        wn.update()
    
    for segment in serpent.segments[2:]:
         if segment.distance(serpent.segments[0])<20:
            for segment in serpent.segments:
                segment.goto(1000,1000)
            serpent.reset()

wn.exitonclick()
    # turtle.Terminator()
    # time.sleep(delay)
