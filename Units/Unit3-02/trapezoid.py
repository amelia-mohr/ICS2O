import decimal
decimal.getcontext().rounding = decimal.ROUND_HALF_UP
finished = False 
while not finished:
    try:
        a = float(input("Please enter a length for side a: "))
        if a <= 0:
            raise ValueError
        b = float(input("Please enter a length for side b: "))
        if b <= 0:
            raise ValueError
        h = float(input("Please enter a height: "))
        if h <= 0:
            raise ValueError
        u = str(input("Please enter a unit (ex. cm, ft, etc.): "))
        a = decimal.Decimal(a)
        b = decimal.Decimal(b)
        h = decimal.Decimal(h)
        calc = ((a + b)/2)*h
        area = round(calc, 2)
        print("All results are rounded to 2 decimal places.")
        print("The area of your circle is: " + str(area) + " " + u + "²")
        finished = True
    except ValueError:
        print("Please enter a POSITIVE NUMBER!")