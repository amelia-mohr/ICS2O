import decimal
decimal.getcontext().rounding = decimal.ROUND_HALF_UP

def sidea():
    finished = False
    while not finished:
        a = float(input("Please enter a length for base a of your trapezoid: "))
        if a <= 0:
            print("Please enter a POSITIVE NUMBER!")
        else: 
            finished = True
    return a

def sideb():
    finished = False
    while not finished:
        b = float(input("Please enter a length for base b of your trapezoid: "))
        if b <= 0:
            print("Please enter a POSITIVE NUMBER!")
        else: 
            finished = True
    return b

def height():
    finished = False
    while not finished:
        h = float(input("Please enter a height for your trapezoid: "))
        if h <= 0:
            print("Please enter a POSITIVE NUMBER!")
        else: 
            finished = True
    return h

area = ((sidea() + sideb())/2) * height()
final = round(decimal.Decimal(str(area)), 2)
print("The area of your trapezoid is: " + str(final))
