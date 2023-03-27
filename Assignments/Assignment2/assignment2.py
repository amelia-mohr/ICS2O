import math
pi = math.pi
finished = False 
while not finished:
    try:
        d = float(input("Please enter a diameter: "))
        if d <= 0:
            raise ValueError
        u = str(input("Please enter a unit (ex. cm, ft, etc.): "))
        r = str(d / 2)
        if r[len(r)-1] == 5:
            r = r[len(r)-1] + 1
            print(r)
        finished = True
    except ValueError:
        print("Please enter a POSITIVE NUMBER!")
