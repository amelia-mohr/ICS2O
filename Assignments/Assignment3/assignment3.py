import decimal
decimal.getcontext().rounding = decimal.ROUND_HALF_UP
pizzas = []

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

def toppings():
    ntopping = int(0)
    for a in range(1, 5):
        if a == 1:
            ttype = 'Onions'
        elif a == 2:
            ttype = 'Pepperoni'
        elif a == 3:
            ttype = 'Bacon'
        elif a == 4:
            ttype = 'Olives'
        print("Do you want " + ttype + " on your pizza?")
        finished = False
        while not finished:
            topping = input("   Type 'y' for yes or 'n' for no: ")
            if topping == 'y':
                ntopping = ntopping + 1
                finished = True 
            elif topping == 'n':
                finished = True
            else: 
                print("Please enter 'y' for yes or 'n' for no.")
    if ntopping == 1:
        tcost = float(1.00)
    elif ntopping == 2:
        tcost = float(1.75)
    elif ntopping == 3:
        tcost = float(2.50)
    elif ntopping == 4:
        tcost = float(3.35)
    elif ntopping == 0:
        tcost = float(0)
    return tcost

def remove():
    print("Your Items:")
    y = 0
    for x in pizzas:
        y = y + 1
        print("   Item " + str(y) + " - $" + str(x))
    print("Would you like to remove a pizza?")
    finished = False
    while not finished:
        yorn = input("   Type 'y' for yes or 'n' for no: ")
        if yorn == 'y':
            complete = False
            while not complete:
                print("Your Items:")
                y = 0
                for x in pizzas:
                    y = y + 1
                    print("   Item " + str(y) + " - $" + str(x))
                z = int(input("Please enter the number of the item you would like to remove: "))
                w = z - 1
                if w < 0 or w >= len(pizzas):
                    print("Invalid item number!")
                else: 
                    print("You've removed: Item " + str(z))
                    print("Price: $" + str(pizzas[w]))
                    pizzas.pop(w)
                    more()
                    remove()
                    complete = True
            finished = True
        elif yorn == 'n':
            pass
            finished = True
        else: 
            print("Please enter 'y' for yes or 'n' for no.")

def more():
    print("Your Items:")
    y = 0
    for x in pizzas:
        y = y + 1
        print("   Item " + str(y) + " - $" + str(x))
    print("Would you like to order another pizza?")
    finished = False
    while not finished:
        answer = input("   Type 'y' for yes or 'n' for no: ")
        if answer == 'y':
            print("Cost: $" + str(pretotal()))
            more()
            finished = True
        elif answer == 'n':
            pass
            finished = True
        else:
            print("Please enter 'y' for yes or 'n' for no.")

def pretotal():
    price = psize() + toppings()
    pretotal = round(decimal.Decimal(str(price)), 2)
    pizzas.append(pretotal)
    return pretotal

def subtotal():
    price = sum(pizzas)
    subtotal = round(decimal.Decimal(str(price)), 2)
    return subtotal

def tax():
    p = sum(pizzas)
    tax = round(decimal.Decimal(float(p) * 0.13), 2)
    return tax

def total():
    p = sum(pizzas)
    total = round(decimal.Decimal(float(p) * 1.13), 2)
    return total

y = 0
print("Hello!")
print("Welcome to Pizza Code!")
print("Cost: $" + str(pretotal()))
more()
remove()
print("Final " + str(len(pizzas)) + " Item(s): ")
for x in pizzas:
    y = y + 1
    print("   Item " + str(y) + " - $" + str(x))
print("Subtotal: $" + str(subtotal()))
print("Tax: $" + str(tax()))
print("Total: $" + str(total()))
print("Thank you for buying from Pizza Code!")
