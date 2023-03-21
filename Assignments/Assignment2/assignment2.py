import math

d = float(input("Please enter a diameter: "))
r = round(d / 2, 2)
area = round(math.pi * (r ** 2), 2)
circumference = round(2 * math.pi * r, 2)
print("All results (except of the diameter) are rounded to 2 decimal places.")
print("The diameter of your circle is: " + str(d))
print("The radius of your circle is: " + str(r))
print("The area of your circle is: " + str(area))
print("And the circumference of your circle is: " + str(circumference))
