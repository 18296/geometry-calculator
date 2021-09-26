import turtle
import math

def regular_polygons():
  while True:
    no_sides = int(input("how many sides does your shape have?"))
    for repeats in range(no_sides): # draws diagram
      turtle.forward(100)
      turtle.left((360/no_sides))




# start of code
while True:
    select = input("what area would you like to calculate?: Regular polygon (1) Circles (2) Triangles (3)")
    if select == "1":
        regular_polygons()
    if select == "2":
        pass
    if select == "3":
        pass
