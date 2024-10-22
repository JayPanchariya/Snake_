#importing important libraries
import turtle 
import tkinter as tk
import time
import random
import food as food2

delay=0.1
score=0
high_score=0

#set up for game
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("yellow")
# the width and height can be put as user's choice
wn.setup(width=700, height=700)
wn.tracer(0)        #Turns off the screen updates

#snake head
head=turtle.Turtle()
head.speed(0)
head.shape('circle')
head.color('black')
head.penup()
head.goto(0,0)
head.direction="up"

play_gif="food_lover.gif"
turtle.register_shape(play_gif)
#snake food
food=turtle.Turtle()
food.shape(play_gif)
food.shapesize(stretch_wid=0.05, stretch_len=0.05)
food.speed(0)

# food.shape('triangle')
food.shapesize(stretch_wid=1, stretch_len=1)
food.color('pink')
food.penup()
food.goto(0,60)

Body_seg=[]

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color('green')
pen.penup()
pen.hideturtle()
pen.goto(0,310)
pen.write("Score:0      High Score:0", align='center',font=('Courier',40,'normal'))


#Important functions
def move():
   if head.direction=="up":
      y=head.ycor()
      head.sety(y+20)
   if head.direction=='down':
      y=head.ycor()
      head.sety(y-20)
   if head.direction=='left':
      x=head.xcor()
      head.setx(x-20)
   if head.direction=='right':
      x=head.xcor()
      head.setx(x+20)  
   # if head.direction=="stop":
   #    x=head.xcor()
   #    y=head.ycor() 
   #    head.goto(x,y)         

def go_up(): 
   if head.direction!='down':
      head.direction='up'     
def go_down(): 
   if head.direction!='up':
      head.direction='down'     
def go_left(): 
   if head.direction!='right':
      head.direction='left'     
def go_right():
   if head.direction!='left': 
       head.direction='right'  
# def stop():
#    head.direction="stop"       

#keyboard bindings
wn.listen()   #listen for key press on keyboard
wn.onkeypress(go_up,'w')  
wn.onkeypress(go_down,'s') 
wn.onkeypress(go_left,'a') 
wn.onkeypress(go_right,'d')
# wn.onkeypress(stop,'g')


while True:
   wn.update()
 
 #check for the collision with boundry
   if head.xcor()>340 or head.xcor()<-340 or head.ycor()>340 or head.ycor()<-340:
      time.sleep(1)
      head.goto(0,0)
      head.direction="stop"
    #hide the segments
      for segment in Body_seg:
         segment.goto(1000,1000)
    #clear the segment list
      Body_seg.clear()
    #update score
      score=0  
      pen.clear()
      pen.write("Score:{}     High Score:{} ".format(score,high_score), align='center',font=('Courier',40,'normal'))

      #update time delay
      delay=0.1
   
   #check for collision with food
   if head.distance(food)<20:
      #move food to random spots
      x=random.randint(-340,340)
      y=random.randint(-340,340)
      food.goto(x,y)

      #adding segment
      new_segment=turtle.Turtle()
      new_segment.speed(0)
      new_segment.shape("circle")
      new_segment.color("gray")
      new_segment.penup()
      Body_seg.append(new_segment)
      
      #increase the speed
      delay-=.001

      #increase the score
      score+=10
      
      if score>high_score:
         high_score=score

      pen.clear()
      pen.write("Score:{}     High Score:{} ".format(score,high_score), align='center',font=('Courier',40,'normal'))   

      #move the end segment first   
   for idx in range((len(Body_seg))-1,0,-1):
      x=  Body_seg[idx-1].xcor()
      y=  Body_seg[idx-1].ycor()
      Body_seg[idx].goto(x,y)

   #move segment 0 with the head
   if len(Body_seg)>0:
      x=head.xcor()
      y=head.ycor()
      Body_seg[0].goto(x,y)

  


   move()

   #check for collision with food
   for segment in Body_seg:

      if segment.distance(head)<20:
         time.sleep(1)
         head.goto(0,0)
         head.direction="stop"

      #hide the segments
         for segment in Body_seg:
            segment.goto(1000,1000)
         #clear the segment list
         Body_seg.clear()

      #reset the score
         score=0
      #update time delay
         delay=0.1

         pen.clear()
         pen.write("Score:{}     High Score:{} ".format(score,high_score), align='center',font=('Courier',40,'normal'))   

      
   turtle.Terminator()
   time.sleep(delay)

wn.mainloop()