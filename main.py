import turtle
import mpmath as math
yes = ["yes","y"]
no = ["no", "n"]

library = {}


def diagram(shape, n,values):
  turtle.clearscreen()
  if shape == "polgon":
    a = 400/n
    turtle. begin_fill()
    turtle.fillcolor("dark grey")
    for repeats in range(n): 
      turtle.forward(a)
      turtle.left((360/n))
    turtle.end_fill()

    turtle.forward(a/2)
    turtle.write(values[0])
    turtle.left(90)

    angle = ((((n-2)*180)/n)/2)*(math.pi/180)
    r = (a/2)*(math.tan(angle))

    turtle.forward(r/2)
    turtle.write(values[1]) # draws diagram
    turtle.forward(r/2)

  
    turtle.pensize(2)
    turtle.dot()
    turtle.pensize(1)

    turtle.pencolor("grey")
    turtle.write(values[2])
    turtle.pencolor("black")
  

    int_angle = (180-((angle*(180/math.pi))*2))
    turtle.right(int_angle)

    R = r*math.sec(math.pi/n)

    turtle.forward(R/2)
    turtle.write(values[3])
    turtle.forward(R/2)
    turtle.left(90)
    turtle.circle(R)
    turtle.write(values[4])

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

  a,r,A,R,C = (round(a,2)),(round(r,2)),(round(A,2)),(round(R,2)),(round(C,2))
  listB = [a,r,A,R,C]
  diagram("polgon",n,listB)
  print("R:",R,"P:",P,"a:",a,"C:",C,"A:",A,"r:",r, "\n(rounded to 2 d.p.)")
  
  

def regular_polygons():
  while True:
    try:
      n = int(input("how many sides does your shape have?\t"))
      if n < 3:
        print("2 dimentional shapes must have >2 sides")
        int("a") # breaks code to except condition
      listA = ["  a","   r","A","R","C"]
      diagram("polgon",n,listA)
      break

    except:
      print("please enter a valid number")
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
while True:
  regular_polygons()