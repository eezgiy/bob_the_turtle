from turtle import Turtle,Screen
from square import Square
from draw_dashed_line import DrawDashedLine
from shapes import Shapes
from random_walk import RandomWalk
from spirograph import Spirograph

bob_the_turtle = Turtle()

#change the shape as a turtle
bob_the_turtle.shape("turtle")

#change the color of turtle
bob_the_turtle.color("DarkOliveGreen4")

#speed

bob_the_turtle.speed("fastest")

#draw a square

'''

square = Square(bob_the_turtle) 
square.draw_a_square()

'''

#draw dashed line

'''
draw_dashed_line = DrawDashedLine(bob_the_turtle)
draw_dashed_line.draw_dashed_line()

'''

#draw different shapes

'''
shapes = Shapes(bob_the_turtle)
shapes.draw_different_shapes()

'''
#walk randomly

'''
bob_the_turtle.pensize(5)
random_walk = RandomWalk(bob_the_turtle)
random_walk.random_walk()

'''

#draw a spirograph
'''
draw_spirograph = Spirograph(bob_the_turtle)
random_walk.random_walk()
'''

a_spirograph = Spirograph(bob_the_turtle)
a_spirograph.draw_a_spirograph()

screen = Screen()
#show up the screen
screen.exitonclick()



