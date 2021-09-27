import turtle
import mpmath as math

library = {}


def shape_drawing(shape, n):
  if shape == "polgon":
    for repeats in range(n): 
      turtle.forward(100)
      turtle.left((360/n))

    turtle.forward(50)
    turtle.write("   a")
    turtle.left(90)
    angle = ((((n-2)*180)/n)/2)*(math.pi/180)
    r = (100/2)*(math.tan(angle))
    turtle.forward(r/2)
    turtle.write("  r") # draws diagram
    turtle.forward(r/2)
    R = r*math.sec(math.pi/n)
    turtle.forward(R/2)
    turtle.write("  R")
    turtle.forward(R/2)
    turtle.left(90)
    turtle.circle(R)
    turtle.write("     C")




def polygon_maths(value, type,n):
  angle = ((((n-2)*180)/n)/2)*(math.pi/180)


  if type == "r":
    r = value

  if type == "a":
    a = value
    r = (1/2)*a*math.cot(math.pi/n)

  if type == "A":
    A = value
    a = (A/n)/10
    r = (1/2)*a*math.cot(math.pi/n)

  if type == "R":
    R = value
    r = R*math.cos(math.pi/n)
  
  if type == "C":
    C = value
    R = (C/(2*math.pi))
    r = R*math.cos(math.pi/n)


  A = n*r*2*math.tan(math.pi/n)*10

  a = (r/(math.tan(angle)))*2

  P = a*n

  R = r*math.sec(math.pi/n)

  C = 2*math.pi*R
    
  print(R,P,a,C,A,r)
  
  




def regular_polygons():
  while True:
    try:
      n = int(input("how many as does your shape have?"))
      if n < 3:
        int("a") # breaks code to except condition
      shape_drawing("polgon",n)
      
      break

    except:
      pass
    
  choice = input("write in given variables format: area:1, a:2")
  data = choice.split(",")
  for pair in data:
    key = pair.split(":")[0]
    value = pair.split(":")[1]
    library[key] = value

  if "r" in library:
    r = int(library.get("r"))
    polygon_maths(r,"r",n)

  if "a" in library:
    a = int(library.get("a"))
    polygon_maths(a,"a",n)

  if "A" in library:
    A = int(library.get("A"))
    polygon_maths(A,"A",n)

  if "R" in library:
    R = int(library.get("R"))
    polygon_maths(R,"R",n)
  
  if "C" in library:
    C = int(library.get("C"))
    polygon_maths(C,"C",n)




# start of code
while True:
    select = input("what would you like to calculate?: Regular polygon (1) Circles (2) Triangles (3)")
    if select == "1":
        regular_polygons()
    if select == "2":
        pass
    if select == "3":
        pass
