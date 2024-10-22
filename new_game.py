#importing important libraries
import turtle 
import tkinter as tk
import time
import random

delay=0.1
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



#snake food
food=turtle.Turtle()
food.speed(0)
food.shape('triangle')
food.color('pink')
food.penup()
food.goto(0,60)
#creating segment

# Segments=[]


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

def go_up(): 
   head.direction='up'     
def go_down(): 
   head.direction='down'     
def go_left(): 
   head.direction='left'     
def go_right(): 
   head.direction='right'  

#keyboard bindings
wn.listen()   #listen for key press on keyboard
wn.onkeypress(go_up,'w')  
wn.onkeypress(go_down,'s') 
wn.onkeypress(go_left,'a')     
wn.onkeypress(go_right,'d') 

Segments=[]
# #main game loop

while True:
   wn.update()
   #check for the collision with boundry
   if head.xcor()>320 or head.xcor()<-320 or head.ycor()>320 or head.ycor()<-320:
      time.sleep(1)
      head.goto(0,0)
      head.direction="stop"
    #hide the segments
      for segment in Segments:
         segment.goto(1000,1000)
    #clear the segment list
      Segments.clear()

   if head.distance(food)<20:
      #move food to random spots
      x=random.randint(-320,320)
      y=random.randint(-320,320)
      food.goto(x,y)
   #adding segment
      new_segment=turtle.Turtle()
      new_segment.speed(0)
      new_segment.shape("circle")
      new_segment.color("gray")
      new_segment.penup()
      Segments.append(new_segment)
   #move the end segment first
   
   for idx in range((len(Segments))-1,0,-1):
      # if len(Segments)>2:
      #    x=Segments[idx-1].xcor()
      #    y=Segments[idx-1].ycor()
      #    Segments[idx].goto(x,y)
      if len(Segments)>=1:
         x=Segments[idx].xcor()
         y=Segments[idx].ycor()
         Segments[idx].goto(x,y)   
   
        #move segment 0 with the head
   for i in range(len(Segments)):     
      if len(Segments)>0:
         x=head.xcor()
         y=head.ycor()
         Segments[i].goto(x,y)
         i+=1

      
   move()
   turtle.Terminator()
   time.sleep(delay)
   # print('sanjay')
   # wn.mainloop()