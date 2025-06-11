import math

def calculate_circumference(radius):
  return 2 * math.pi * radius
radius = float(input("Enter the radius of the circle: "))
circumference=calculate_circumference(radius)
print(f" the circumference of the circle is {circumference}")