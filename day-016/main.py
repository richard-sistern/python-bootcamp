from turtle import Turtle 

# Fixes following error:
#  no display name and no $DISPLAY environment variable
import os
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

t = Turtle() # Classes use Pascal case

print(t)