import math
import decimal
finished = False
while not finished:
    try: 
        print("Do you want a Large ($6.00) or Extra Large ($10.00) pizza?")
        size = input("Answer here (L/XL): ")
        if size == 'L':
            t = input("Do you want toppings (yes/no)? ")
            if t == 'yes':
                t1 = input("Do you want Onions ($1.00) (yes/no)? ")
                if t1 == 'yes':
                    price = 6.00 + 1.00
                elif t1 == 'no': 
                    price = 6.00
                else:
                    raise NameError
                t2 = input("Do you want Pepperoni ($1.75) (yes/no)? ")
                if t2 == 'yes':
                    price = price + 1.75
                elif t2 == 'no': 
                    pass
                else:
                    raise NameError  
                t3 = input("Do you want Bacon ($2.50) (yes/no)? ")
                if t3 == 'yes':
                    price = price + 2.50
                elif t3 == 'no': 
                    pass
                else:
                    raise NameError
                t4 = input("Do you want Olives ($3.35) (yes/no)? ")
                if t4 == 'yes':
                    price = price + 3.35
                elif t4 == 'no': 
                    pass
                else:
                    raise NameError
            elif t == 'no':
                price = 6.00
            else:
                raise NameError
        elif size == 'XL':
            t = input("Do you want toppings (yes/no)? ")
            if t == 'yes':
                t1 = input("Do you want Onions ($1.00) (yes/no)? ")
                if t1 == 'yes':
                    price = 10.00 + 1.00
                elif t1 == 'no': 
                    price = 10.00
                else:
                    raise NameError
                t2 = input("Do you want Pepperoni ($1.75) (yes/no)? ")
                if t2 == 'yes':
                    price = price + 1.75
                elif t2 == 'no': 
                    pass
                else:
                    raise NameError
                t3 = input("Do you want Bacon ($2.50) (yes/no)? ")
                if t3 == 'yes':
                    price = price + 2.50
                elif t3 == 'no': 
                    pass
                else:
                    raise NameError
                t4 = input("Do you want Olives ($3.35) (yes/no)? ")
                if t4 == 'yes':
                    price = price + 3.35
                elif t4 == 'no': 
                    pass
                else:
                    raise NameError
            elif t == 'no':
                price = 10.00
            else:
                raise NameError
        else:
            raise NameError
    except NameError:
        print("Please enter an input indicated in the last brackets!")
    else:
        decimal.getcontext().rounding = decimal.ROUND_HALF_UP
        p = round(decimal.Decimal(str(price * 1.13)), 2)
        print("Your pizza is: $" + str(p))
        print("Do you want another pizza?")
        more = input("Answer here (yes/no): ")
        if more == 'yes':
            #pizzas.append(price)
            #for x in pizzas:
                #print("$" + str(x))
            #pizzas.append(price)
            #total = sum(pizzas) * 1.13
            #for x in pizzas:
                #print("Your " + len(pizzas) + "items cost: ")
                #print("   $" + str(x))
            #print("And your total is: $" + str(total))
        elif more == 'no':
            price = round(decimal.Decimal(price * 1.13), 2)
            print("Your total is: $" + str(price))
            print("Thank you for buying our pizzas!")
            finished = True
