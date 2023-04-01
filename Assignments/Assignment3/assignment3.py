import decimal
pizzas = []
scost = float(0)

def psize():
    print("Do you want a Large ($6.00) or Extra Large ($10.00) pizza?")
    finished = False
    while not finished: 
        size = input("   Type 'l' for Large or 'xl' for Extra Large: ")
        if size == 'l':
            scost = float(6.00)
            finished = True
        elif size == 'xl':
            scost = float(10.00)
            finished = True
        else:
            print("Please enter 'l' for Large or 'xl' for Extra Large.")
    return scost
        


while not finished:
    try: 
        print("Do you want a Large ($6.00) or Extra Large ($10.00) pizza?")
        size = input("   Answer here (L/XL): ")
        if size == 'L':
            t = input("Do you want toppings (yes/no)? ")
            if t == 'yes':
                t1 = input("   Do you want Onions ($1.00) (yes/no)? ")
                if t1 == 'yes':
                    price = 6.00 + 1.00
                elif t1 == 'no': 
                    price = 6.00
                t2 = input("   Do you want Pepperoni ($1.75) (yes/no)? ")
                if t2 == 'yes':
                    price = price + 1.75
                elif t2 == 'no': 
                    pass
                t3 = input("   Do you want Bacon ($2.50) (yes/no)? ")
                if t3 == 'yes':
                    price = price + 2.50
                elif t3 == 'no': 
                    pass
                t4 = input("   Do you want Olives ($3.35) (yes/no)? ")
                if t4 == 'yes':
                    price = price + 3.35
                elif t4 == 'no': 
                    pass
            elif t == 'no':
                price = 6.00
        elif size == 'XL':
            t = input("Do you want toppings (yes/no)? ")
            if t == 'yes':
                t1 = input("   Do you want Onions ($1.00) (yes/no)? ")
                if t1 == 'yes':
                    price = 10.00 + 1.00
                elif t1 == 'no': 
                    price = 10.00
                t2 = input("   Do you want Pepperoni ($1.75) (yes/no)? ")
                if t2 == 'yes':
                    price = price + 1.75
                elif t2 == 'no': 
                    pass
                t3 = input("   Do you want Bacon ($2.50) (yes/no)? ")
                if t3 == 'yes':
                    price = price + 2.50
                elif t3 == 'no': 
                    pass
                t4 = input("   Do you want Olives ($3.35) (yes/no)? ")
                if t4 == 'yes':
                    price = price + 3.35
                elif t4 == 'no': 
                    pass
            elif t == 'no':
                price = 10.00
    try:
        decimal.getcontext().rounding = decimal.ROUND_HALF_UP
        pizzas.append(price)
        p = round(decimal.Decimal(str(price)), 2)
        print("Your pizza is: $" + str(p))
        print("   Do you want another pizza?")
        more = input("      Answer here (yes/no): ")
        if more == 'yes':
            print("Your Items:")
            y = 0
            for x in pizzas:
                y = y + 1
                print("   " + str(y) + ": $" + str(x))
        while more == 'no':
            total = round(decimal.Decimal((sum(pizzas)) * 1.13), 2)
            print("Your " + str(len(pizzas)) + " items cost: ")
            y = 0
            for x in pizzas:
                y = y + 1
                print("   " + str(y) + ": $" + str(x))
            remove = input("   Would you like to remove a pizza (yes/no)? ")
            if remove == 'yes':
                print("Your Items:")
                y = 0
                for x in pizzas:
                    y = y + 1
                    print("   " + str(y) + ": $" + str(x))
                z = int(input("Which Item would you like to remove? "))
                z = z - 1
                pizzas.pop(z)
                continue
            elif remove == 'no':
                print("Your final " + str(len(pizzas)) + " items cost: ")
                y = 0
                for x in pizzas:
                    y = y + 1
                print("   " + str(y) + ": $" + str(x))
                print("And your total is: $" + str(total))
                print("Thank you for buying our pizzas!")
                more = 'done'