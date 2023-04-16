from _2dSystem import *
from machine import Pin
import time

left = Pin(15, Pin.IN,Pin.PULL_UP)
right = Pin(14, Pin.IN,Pin.PULL_UP)


delta = 0.00001

pos = Point(0, 0)
character = Object2d(pos, "pass")
speed = 2

def main():
    screen.fill(0)
    
    if left.value() == 0:
        pos.trasform_by_vector(Vector2(-speed, 0)) 
        character.move_now(pos)

    elif right.value() == 0:
        pos.trasform_by_vector(Vector2(speed, 0))
        character.move_now(pos)

    
    character.draw_self_as_str("e")
    screen.show()

while True:
    main()
    time.sleep(delta)