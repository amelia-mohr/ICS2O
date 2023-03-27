import math
pi = math.pi
finished = False 
while not finished:
    try:
        d = float(input("Please enter a diameter: "))
        if d <= 0:
            raise ValueError
        u = str(input("Please enter a unit (ex. cm, ft, etc.): "))
        def round_half_up(n):
            x = str(n)
            if x[4] == 5:
                n = ceil(n, 2)
            return n
        print(round_half_up(0.005))
        r = str(d / 2)
        finished = True
    except ValueError:
        print("Please enter a POSITIVE NUMBER!")
