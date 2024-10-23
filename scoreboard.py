from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score=0
        self.color("blue")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        # self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.write("Score:{}     High Score:{} ".format(self.score,self.high_score), align='center',font=('Courier',25,'normal'))   

    def increase_score(self,increase):
        self.x=increase
        self.score += increase
        if self.score>self.high_score:
         self.high_score=self.score
        self.clear()
        self.update_scoreboard()
    
    def decrease_score(self,increase):
        self.x=increase
        self.score -= increase
        if self.score>self.high_score:
         self.high_score=self.score
        self.clear()
        self.update_scoreboard()
        
    def reset(self):
        self.clear()
        self.score = 0
        self.update_scoreboard()
        
            
    def game_over(self):
        # self.clear()
        print('ss')
        self.write("Game Over     High Score:{} ".format(self.high_score), align='center',font=('Courier',40,'normal'))   
        # self.write("GAME OVER", align="center", font=("Arial", 40, "normal"))
            
    game_over()  