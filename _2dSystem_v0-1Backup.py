"""
Main Library for 2d System. Loosely based on classes and systems of the Godot Game Engine.
"""

from machine import Pin, SoftI2C
import math
import ssd1306
import time

def init_oled(sclPin, sdaPin):   
    i2c = SoftI2C(scl = Pin(sclPin), sda = Pin(sdaPin))
    
    pin = Pin(16, Pin.OUT)
    pin.value(0) 
    pin.value(1)

    oled_width = 128
    oled_height = 64
    oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
    return oled

screen = init_oled(1, 0)

class Point:
    x = 0
    y = 0
    
    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"({self.x}, {self.y})"
    
    #operators
    def is_equal(self, r : Point):
        if self.x == r.x and self.y == r.y:
            return True
        else:
            return False
    
    def trasform_by_vector(self, r : Vector2):
        self.x += r.x
        self.y += r.y
    
    def is_between(self, line : Line2d):
        if self.y == (line.m * self.x + line.c):
            return True
        else:
            return False
    
class Line2d:
    
    def __init__(self, pt1 : Point, pt2: Point):
        self.pt1 = pt1
        self.pt2 = pt2
        #y = mx + c
        self.m = (pt2.y - pt1.y) / (pt2.x - pt1.x)
        self.c = pt1.y - (self.m * pt1.x) 
    
    def __str__(self):
        return f"Line2d from {self.pt1} to {self.pt2}"
    
    def __repr__(self):
        return f"Line2d from {self.pt1} to {self.pt2}"
    
    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
class Area2d:
    #not implemented yet
    pass

class Vector2:
    """
    Simplified implementation of Godot's Vector2 class in micropython.
    """

    x = 0
    y = 0
    
    def __init__(self, xPos : int = 0, yPos: int = 0):
        self.x = xPos
        self.y = yPos
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"({self.x}, {self.y})"
    
    #constants
    def ZERO(self):
        self.x = 0
        self.y = 0
        
    def ONE(self):
        self.x = 1
        self.y = 1
        
    def LEFT(self):
        self.x = -1
        self.y = 0
        
    def RIGHT(self):
        self.x = 1
        self.y = 0
    
    def UP(self):
        self.x = 0
        self.y = -1
    
    def DOWN(self):
        self.x = 0
        self.y = 1
    
    #functions
    def abs(self):
        self.x = abs(self.x)
        self.y = abs(self.y)
        
    def angle_n(self, n : Vector2):
        #prod = a*b
        #return math.asin(prod.abs() / 
        pass
        
    def bounce(self, n : Vector2):
        #i = 
        pass
    
    def direction_to(self, to : Vector2):
        return Vector2(to.x - self.x, to.y - self.y)
    
    def distance_to(self, to : Vector2):
        return ((to.x - self.y) ** 2 + (to.y - self.y) ** 2) ** 0.5
    
    def from_angle(self, angle : float):
        pass
    
    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def move_toward(self, to : Vector2, delta : float):
        pass
    
    def normalized(self):
        if self.x != 0:
            self.x = self.x / abs(self.x)
        else:
            self.x = 0
        
        if self.y != 0:
            self.y = self.y / abs(self.y)
        else:
            self.y = 0
    
    #operators
    def is_equal(self, r : Vector2):
        if self.x == r.x and self.y == r.y:
            return True
        else:
            return False
    
    def multiply_by_vector(self, r : Vector2):
        self.x *= r.x
        self.y *= r.y
    
    def divide_by_vector(self, r : Vector2):
        self.x //= r.x
        self.y //= r.y
    
    def add_by_vector(self, r : Vector2):
        self.x += r.x
        self.y += r.y
    
    def subtract_by_vector(self, r : Vector2):
        self.x -= r.x
        self.y -= r.y
    
    def multiply(self, n : int):
        self.x *= n
        self.y *= n
    
    def divide(self, n : int):
        self.x //= n
        self.y //= n
    
    def add(self, n : int):
        self.x += n
        self.y += n
    
    def subtract(self, n : int):
        self.x -= n
        self.y -= n
    
class Object2d:
    
    def __init__(self, pos : Point, collider):
        self.pos = pos
        self.collider = collider
        #self.texture = texture
    
    def __str__(self):
        return f"Object2d @ ({self.pos.x}, {self.pos.y})"
    
    def __repr__(self):
        return f"Object2d @ ({self.pos.x}, {self.pos.y})"
    
    #functions
    def is_colliding(self, target : Line2d):
        if self.pos.is_equal(target):
            return True
        else:
            return False
    
    def draw_self_as_square(self):
        screen.rect(self.pos.x, self.pos.y, self.pos.x + 10, self.pos.y + 10, 1)
        
    def draw_self_as_str(self, txt : str):
        screen.text(txt, self.pos.x, self.pos.y, 1)
    
    def move_now(self, target : Point):
        self.pos.x = target.x
        self.pos.y = target.y
    
#class Texture:
#	texture class to be implemented soon.
#   def __init__(self, 


    