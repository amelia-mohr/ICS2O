import math
pi = math.pi
d = 0
while d == 0:
    try:
        d = float(input("Please enter a diameter: "))
    except ValueError:
        print("Please enter a NUMBER!")
    continue
    except d <= 0:
        print("Please enter a POSITIVE NUMBER!")
    continue
