import math
pi = math.pi
finished = False 
while not finished:
    try:
        d = float(input("Please enter a diameter: "))
        if d <= 0:
            raise ValueError
        u = str(input("Please enter a unit (ex. cm, ft, etc.): "))
        r = round(d / 2, 2)
        a = round(pi*(r**2))
        c = round(2*pi*r)
        print("All results (except for the diameter) are rounded to 2 decimal places.")
        print("The diameter of your circle is: " + str(d) + " " + u)
        print("The radius of your circle is: " + str(r) + " " + u)
        print("The area of your circle is: " + str(a) + " " + u + "²")
        print("And the circumfrence of your circle is: " + str(c) + " " + u)
        finished = True
    except ValueError:
        print("Please enter a POSITIVE NUMBER!")
