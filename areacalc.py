print "THE CALCULATOR IS STARTING UP!"

option = raw_input("""Enter :
C for Circle,
T for Triangle,
S for Square
R for Rectangle
P for Parallelogram
Z for Trapezoid
E for Ellipse
""").upper()

if option == "C":
  radius = float(raw_input("What is the circle's radius? "))
  print radius
  area = 3.14159 * radius**2
  print "The area is: " + str(area)
elif option == "T":
  base = float(raw_input("Enter a base length: "))
  height = float(raw_input("Enter a height length: "))
  area = base * height / 2
  print "The area is: " + str(area)
elif option == "S":
  side = float(raw_input("Enter a side length: "))
  area = side * side
  print "The area is: " + str(area)
elif option == "R":
  width = float(raw_input("Enter a width length: "))
  height = float(raw_input("Enter a height length: "))
  area = width * height
  print "The area is: " + str(area)
elif option == "P":
  base = float(raw_input("Enter a base length: "))
  height = float(raw_input("Enter a height length: "))
  area = base * height
  print "The area is: " + str(area)
elif option == "Z":
  base1 = float(raw_input("Enter a base length: "))
  base2 = float(raw_input("Enter another base length: "))
  height = float(raw_input("Enter a height length: "))
  area = height / 2 * (base1 + base2)
  print "The area is: " + str(area)
elif option == "E":
  r1 = float(raw_input("What is the ellipse's first radius? "))
  r2 = float(raw_input("What is the ellipse's second radius? "))
  area = 3.14159 * r1 * r2
  print "The area is: " + str(area)
else:
  print ("Shitty input")

print "CALCULATOR OUT!"