from turtle import Turtle
import turtle
import random
class Food(Turtle):
    def __init__(self, width_screen, height_screen):
        super().__init__()
        self. width_screen= width_screen
        self. height_screen= height_screen
        self.m_gif="mouse1.gif"
        self.m_gif2="mouse2.gif"
        turtle.register_shape(self.m_gif)
        turtle.register_shape(self.m_gif2)
        self.shape(self.m_gif)
        self.penup()
        self.a=self.m_gif
    

    def refresh(self):
        x=random.randint(- ((self. width_screen//2)-20),((self. width_screen//2)-20) )
        y=random.randint(-((self. height_screen//2)-20),((self. height_screen//2)-20))
        self.goto(x,y)
    
    def change_gif(self):   # Looping through the 2 gifs
        if self.a==self.m_gif:
            self.shape(self.m_gif2)
            self.a =self.m_gif2
        else:
            self.shape(self.m_gif)
            self.a =self.m_gif
        
        