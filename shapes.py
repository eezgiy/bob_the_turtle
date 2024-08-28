import random

class Shapes:
    
    def __init__ (self,turtle):
            self.turtle = turtle
            
    def get_random_color(self):
        return(random.random(),random.random(),random.random())
            
    def draw_different_shapes(self):
        
        max_sides = 10 
        
        for number_of_sides in range(3, max_sides + 1):
            angle = 360 / number_of_sides  
            
            self.turtle.color(self.get_random_color())
 
            for _ in range(number_of_sides):
                
                self.turtle.forward(100)
                self.turtle.right(angle)
                
            
                
        