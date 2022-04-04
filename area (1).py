'''
Luis felipe Hernandez Almanza
6520150021
EVALUACIÓN Y MEJORA PARA EL DESARROLLO DE SOFTWARE
20/02/2022
Marco Muñoz

This code give the area of the 4 basic figures (Square, Triangule, Circle and Rectangule)

Input:
Write the name of the figure (Square, Triangule, Circle and Rectangule)
    Square

Write the value of its side
    4

Output:

    The area is: 16 cm^2


'''
import math
from unittest import result


def square():
    side = int((input("Write the value of its side: ")))
    side *= side
    print("The area is: ", side, " cm^2")


def trian():
    b = int((input("Write the base: ")))
    h = int((input("Write the high: ")))

    result = (b*h)/2
    print("The area is: ", result," cm^2" )

def rect():
    b = int((input("Write the base: ")))
    h = int((input("Write the high: ")))
    
    b*=h
    print("The area is: ", b," cm^2" )

def circ():
    r = int((input("Write the radius: ")))
    result = math.pi * (r*r)
    print("The area is: ", result," cm^2" )

if __name__ == '__main__':

    fig = (input("Write the name of the figure (Square, Triangule, Circle and Rectangule)").lower())
    
    if fig == "square":
        square()
    elif fig == "triangule":
         trian()
    elif fig == "rectangule":
        rect()
    elif fig == "circle":
        circ()
    else:
        print("You don't fill the fields or you misspelled something, try again")
        
