from turtle import Turtle

STARTING_POSITIONS = [(0,0)]#, (-20,0), (-40,0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
    
    def create_snake(self):
 	# CREATE NEW SEGMENTS OF TYPE TURTLE WITH SQUARE SHAPE, GREEN COLOR IN THE POSITION 		DEFINED IN STARTING POINTS AND APPEND THEM TO THE LIST OF SEGMENTS INSIDE THE SNAKE.
        for position in STARTING_POSITIONS:
            head=Turtle()
            head.speed(0)
            head.shape('circle')
            head.color('black')
            head.penup()
            head.goto(position)
            self.segments.append(head)
    
    def move(self):
	# MOVING THE SEGMENTS ONE AFTER ANOTHER 
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()# YOUR CODE HERE
            new_y = self.segments[seg_num-1].ycor()# YOUR CODE HERE 
            self.segments[seg_num].goto(new_x, new_y)
	# MOVING ONLY THE FIRST SEGMENT	
        self.segments[0].forward(MOVE_DISTANCE)
        #set speed to 0 to make it move instantly
        self.segments[0].speed(0)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
        # WHAT DOES heading ATTRIBUTE STAND FOR ?? WHAT DOES THIS FUNCTION DO?  

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
 
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def short(self):
        current_seg=self.segments.pop()
        current_seg.goto(1000,1000)
    
    def add_segment(self, position):
	# CREATE A NEW SEGMENT AT THE POSITION position, GREEN COLOR AND SQUARE, AND APPEND IT 		TO THE LIST OF SEGMENTS OF THE SNAKE. 
        new_segment=Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("gray")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    def reset(self):
        self.segments.clear()
        self.create_snake()
