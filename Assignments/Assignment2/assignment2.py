import math

while True: 
    try: 
        d = float(input("Please enter a diameter: "))
        if d<0:
            print("Please enter a POSITIVE number!")
        elif d==0:
            print("Please enter a NUMBER!")
        continue
    
    except ValueError:
        print("Please enter a NUMBER!")
        continue
    
    else:
        r = round(d / 2, 2)
        area = round(math.pi * (r ** 2), 2)
        circumference = round(2 * math.pi * r, 2)
    break

print("The diameter of your circle is: " + str(d))
print("The radius of your circle is: " + str(r))
print("The area of your circle is: " + str(area))
print("And the circumference of your circle is: " + str(circumference))
