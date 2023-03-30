import math
import decimal
finished = False
while not finished:
    try: 
        print("Do you want a Large ($6.00) or Extra Large ($10.00) pizza?")
        size = input("Answer here (L or XL): ")
        if size == 'L':
            t = input("Do you want toppings (yes/no)? ")
            if t == 'yes':
                t1 = input("Do you want Onions ($1.00) (yes/no)? ")
                if t1 == 'yes':
                    price = 6.00 + 1.00
                else: 
                    price = 6.00
                t2 = input("Do you want Pepperoni ($1.75) (yes/no)? ")
                if t2 == 'yes':
                    price = price + 1.75
                else: 
                    pass
                t3 = input("Do you want Bacon ($2.50) (yes/no)? ")
                if t3 == 'yes':
                    price = price + 2.50
                else: 
                    pass
                t4 = input("Do you want Olives ($3.35) (yes/no)? ")
                if t4 == 'yes':
                    price = price + 3.35
                else: 
                    pass
            else:
                price = 6.00
        elif size == 'XL':
            t = input("Do you want toppings (yes/no)? ")
            if t == 'yes':
                t1 = input("Do you want Onions ($1.00) (yes/no)? ")
                if t1 == 'yes':
                    price2 = 10.00 + 1.00
                else: 
                    price2 = 10.00
                t2 = input("Do you want Pepperoni ($1.75) (yes/no)? ")
                if t2 == 'yes':
                    price2 = price2 + 1.75
                else: 
                    pass
                t3 = input("Do you want Bacon ($2.50) (yes/no)? ")
                if t3 == 'yes':
                    price2 = price2 + 2.50
                else: 
                    pass
                t4 = input("Do you want Olives ($3.35) (yes/no)? ")
                if t4 == 'yes':
                    price2 = price2 + 3.35
                else: 
                    pass
            else:
                price2 = 10.00
    finally:
        decimal.getcontext().rounding = decimal.ROUND_HALF_UP
        if size == 'L':
            price = round(decimal.Decimal(price * 1.13), 2)
            print("Your total is: $" + str(price))
        elif size == 'XL':
            price2 = round(decimal.Decimal(price2 * 1.13), 2)
            print("Your total is: $" + str(price2))
        print("Do you want another pizza?")
        more = input("Answer here (yes/no): ")
        if more == 'yes':
            finished = False
        elif more == 'no':
            print("Thank you for buying a pizza!")
            finished = True
