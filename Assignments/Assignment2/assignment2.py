import math
pi = math.pi
finished = False 
while not finished:
    try:
        d = float(input("Please enter a diameter: "))
        if d <= 0:
            raise ValueError
        u = str(input("Please enter a unit (ex. cm, ft, etc.): "))
        def round_half_up(n, y):
            multiplier = 10 ** y
            return math.floor(n*multiplier + 0.5) / multiplier
        r = str(d / 2)
        print(round_half_up(0.285, 2))
        finished = True
    except ValueError:
        print("Please enter a POSITIVE NUMBER!")
