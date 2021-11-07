# importing the library
from turtle import *

# Avegrers emblem
# Circles

speed(10)
penup()
goto(0, -300)
pendown()
color("black", "white")
circle(300, 360)
penup()
goto(0, -250)
pendown()
circle(250, 360)
penup()
speed(3)

# Letter A
begin_fill()
goto(-180, -320)
pendown()
left(65)
forward(250)
right(65)
forward(140)
right(90)
forward(20)
left(135)
forward(80)
left(90)
forward(80)
left(135)
forward(20)
right(90)
forward(110)
right(115)
forward(260)
right(155)
forward(190)
left(45)
forward(80)
left(135)
forward(365)
left(90)
forward(70)
left(65)
forward(721)
left(115)
forward(73)

end_fill()
penup()

#last triangle

goto(65, -135)
pendown()
left(45)
forward(80)
right(135)
forward(56)
right(90)
forward(56)

penup()
goto(1000, 1000)

# ASSEMBLE

for x in range(0, 10):
    print( "AVENGERS! ASSEMBLE!" )

done()