from turtle import Turtle
import turtle
import random

class Insect(Turtle):
    def __init__(self, width_screen, height_screen):
        super().__init__()
        self. width_screen= width_screen
        self. height_screen= height_screen
        play_gif="centipede.gif"
        turtle.register_shape(play_gif)
        self.shape(play_gif)
        self.penup()
        self.color("red")
    
        self.shapesize(stretch_wid=10, stretch_len=10)
        self.speed("fastest")
        self.goto(0,160)

    def refresh(self):
        x=random.randint(- ((self. width_screen//2)-10),((self. width_screen//2)-10) )
        y=random.randint(-((self. height_screen//2)-10),((self. height_screen//2)-10))
        self.goto(x,y)    
    