from turtle import Turtle, Screen 

# Fixes following error:
#  no display name and no $DISPLAY environment variable
import os
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

t = Turtle() # Classes use Pascal case

print(t)
t.shape("turtle")
t.color("coral")
t.forward(100)

s = Screen()
print(s.canvheight)
s.exitonclick()