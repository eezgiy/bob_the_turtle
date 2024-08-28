class Square:
    
    def __init__ (self,turtle):
        self.turtle = turtle
    
    def draw_a_square(self):   
        for _ in range(4):
            self.turtle.forward(150)
            self.turtle.right(90)
    