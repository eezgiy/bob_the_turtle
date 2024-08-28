class DrawDashedLine:
    
    def __init__ (self,turtle):
            self.turtle = turtle
        
    def draw_dashed_line(self):
        
        for _ in range(8):
            self.turtle.forward(10)
            self.turtle.penup()
            self.turtle.forward(10)
            self.turtle.pendown()