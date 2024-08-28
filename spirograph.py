import random

class Spirograph:
    
    def __init__ (self,turtle):
        self.turtle = turtle
    
    def get_random_color(self):
        return(random.random(),random.random(),random.random())
    
    def draw_a_spirograph(self):
        
        for _ in range(75):
        
            self.turtle.color(self.get_random_color())
            self.turtle.circle(120)
            self.turtle.setheading(self.turtle.heading()+ 10)