import random

class RandomWalk:
    
    def __init__ (self,turtle):
        self.turtle = turtle
    
    def get_random_color(self):
        
        return(random.random(),random.random(),random.random())
    '''
       r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        random_color = (r,g,b)
        return random_color
    '''
    
    def random_walk(self):
        direction_angles = [0,75,90,150,180]
    
        for _ in range(75):
            self.turtle.forward(100)
            direction = random.choice(direction_angles)
            
            if direction == 0 or direction == 90:
                self.turtle.right(direction)
                self.turtle.color(self.get_random_color())
            else:
                self.turtle.left(direction)
                self.turtle.color(self.get_random_color())