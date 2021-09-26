import turtle
import math
library = {}


def shape_drawing(shape, no_sides):
  if shape == "polgon":
    for repeats in range(no_sides): 
      turtle.forward(100)
      turtle.left((360/no_sides))

    turtle.forward(50)
    turtle.write("perimeter")
    turtle.left(90)
    angle = ((((no_sides-2)*180)/no_sides)/2)*(math.pi/180)
    apothem = (100/2)*(math.tan(angle))
    turtle.forward(apothem)
    turtle.write("apothem") # draws diagram




def polygon_maths(value, type):
  if type == "area":
    print(value)

  if type == "apothem":
    print(value)

  if type == "perimeter":
    print(value) # figure the math out later
  
  




def regular_polygons():
  while True:
    try:
      no_sides = int(input("how many sides does your shape have?"))
      if no_sides < 3:
        int("a") # breaks code to except condition
      shape_drawing("polgon",no_sides)
      
      break

    except:
      pass
    
  choice = input("write in given variables format: area:1, side:2")
  data = choice.split(",")
  for pair in data:
    print("pair:", pair)
    key = pair.split(":")[0]
    value = pair.split(":")[1]
    library[key] = value

  if "area" in library:
    polygon_maths(library.get("area"),"area") 

  if "apothem" in library:
    polygon_maths(library.get("apothem"),"apothem")

  if "perimeter" in library:
    polygon_maths(library.get("perimeter"),"perimeter")




# start of code
while True:
    select = input("what area would you like to calculate?: Regular polygon (1) Circles (2) Triangles (3)")
    if select == "1":
        regular_polygons()
    if select == "2":
        pass
    if select == "3":
        pass
