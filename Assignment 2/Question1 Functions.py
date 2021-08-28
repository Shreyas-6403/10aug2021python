#Write a program to print the area of Oval,Triangle,Rectangle,Pentagon,Hexagon,Trapezium,& Circle 
# in this program you must be use package & modules,functions,exceptions.

import math
from math import sqrt

def Oval(major,minor):
    return(3.141592 * major * minor)

def Tri(b,h):
    return (0.5*b*h)

def Rect(l,breadth):
    return (l*breadth)

def Penta(a):
    return (sqrt(5 * (5 + 2 * (sqrt(5)))) * a * a) / 4

def Hexagon(s):
    return ((3 * math.sqrt(3) *(s * s)) / 2)

def Trapezium(area,bre,height):
    return (0.5*(area+bre)*height)

def Circle(PI,r):
    return (PI*r*r)