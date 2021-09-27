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

    A = n*r*2*math.tan(math.pi/n)*10

    
    a = (value/(math.tan(angle)))*2
    # a = (A/n)/10


    P = a*n
    

    R = value*math.sec(math.pi/n)

    C = 2*math.pi*R
    
    print(R,P,a,C,A)



  if type == "a":
    print(value) # figure the math out later
  
  




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




# start of code
while True:
    select = input("what would you like to calculate?: Regular polygon (1) Circles (2) Triangles (3)")
    if select == "1":
        regular_polygons()
    if select == "2":
        pass
    if select == "3":
        pass
