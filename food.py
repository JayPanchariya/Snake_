from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self, width_screen, height_screen):
        super().__init__()
        self. width_screen= width_screen
        self. height_screen= height_screen
        self.shape("triangle")
        self.penup()
        self.color("pink")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.speed("fastest")
        # What does the previous lines do? 
        # create 2 random integers as coordinates, and move the turtle circle object there.  
        # you can use random.randit and Turtle.goto(.) 
        # YOUR CODE HERE 

    def refresh(self):
        x=random.randint(- ((self. width_screen//2)-10),((self. width_screen//2)-10) )
        y=random.randint(-((self. height_screen//2)-10),((self. height_screen//2)-10))
        self.goto(x,y)
            # create 2 random integers as coordinates, and move the turtle circle object there.  
        # you can use random.randit and Turtle.goto(.) 
        # YOUR CODE HERE




