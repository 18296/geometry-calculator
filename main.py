import turtle
import math
library = {}

def regular_polygons():
  while True:
    try:
      no_sides = int(input("how many sides does your shape have?"))
      if no_sides < 3:
        int("a") # breaks code to except condition
      for repeats in range(no_sides): 
        turtle.forward(100)
        turtle.left((360/no_sides))
      turtle.forward(50)
      turtle.write("side")
      turtle.left(90)
      angle = ((((no_sides-2)*180)/no_sides)/2)*(math.pi/180)
      apothem = (100/2)*(math.tan(angle))
      turtle.forward(apothem)
      turtle.write("apothem") # draws diagram
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
    print(library)

  




# start of code
while True:
    select = input("what area would you like to calculate?: Regular polygon (1) Circles (2) Triangles (3)")
    if select == "1":
        regular_polygons()
    if select == "2":
        pass
    if select == "3":
        pass
