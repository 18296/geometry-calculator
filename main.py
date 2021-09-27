import turtle
import mpmath as math

library = {}

def diagram(shape, n):
  if shape == "polgon":
    a = 400/n
    turtle. begin_fill()
    turtle.fillcolor("dark grey")
    for repeats in range(n): 
      turtle.forward(a)
      turtle.left((360/n))
    turtle.end_fill()

    turtle.forward(a/2)
    turtle.write("   a")
    turtle.left(90)

    angle = ((((n-2)*180)/n)/2)*(math.pi/180)
    r = (a/2)*(math.tan(angle))

    turtle.forward(r/2)
    turtle.write("  r") # draws diagram
    turtle.forward(r/2)

  
    turtle.pensize(2)
    turtle.dot()
    turtle.pensize(1)

    turtle.pencolor("grey")
    turtle.write("  A")
    turtle.pencolor("black")
  

    int_angle = (180-((angle*(180/math.pi))*2))
    turtle.right(int_angle)

    R = r*math.sec(math.pi/n)

    turtle.forward(R/2)
    turtle.write("  R")
    turtle.forward(R/2)
    turtle.left(90)
    turtle.circle(R)
    turtle.write("     C")

    turtle.hideturtle()



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

  print("R:",R,"P:",P,"a:",a,"C:",C,"A:",A,"r:",r)
  
  

def regular_polygons():
  while True:
    try:
      n = int(input("how many sides does your shape have?"))
      if n < 3:
        int("a") # breaks code to except condition
      diagram("polgon",n)
      
      break

    except:
      pass

  while True:
    try:

      choice = input("write given variables in format: known:value \t")
      key = choice.split(":")[0]
      value = choice.split(":")[1]
      library[key] = value


      if key in library:
        value = int(library.get(key))
        polygon_maths(value,key,n)
      break
    except:
      pass


# start of code
regular_polygons()