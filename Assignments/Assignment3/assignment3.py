import decimal
decimal.getcontext().rounding = decimal.ROUND_HALF_UP
pizzas = []
scost = float(0)
tcost = float(0)
pretotal = float(0)
total = float(0)

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

def pretotal():
    price = psize() + toppings()
    pretotal = round(decimal.Decimal(str(price)), 2)
    pizzas.append(pretotal)
    return pretotal

def remove():
    print("Would you like to remove a pizza?")
    finished = False
    while not finished:
        yorn = input("   Type 'y' for yes or 'n' for no: ")
        if yorn == 'y':
            print("Your Items:")
            y = 0
            for x in pizzas:
                y = y + 1
                print("   Item " + str(y) + "- $" + str(x))
            z = int(input("Please enter the number of the item you would like to remove: "))
            z = z - 1
            pizzas.pop(z)
            print(more())
            print(remove())
            finished = True
        elif yorn == 'n':
            pass
            finished = True
        else: 
            print("Please enter 'y' for yes or 'n' for no.")

def more():
    print("Would you like another pizza?")
    finished = False
    while not finished:
        answer = input("   Type 'y' for yes or 'n' for no: ")
        if answer == 'y':
            print("Your pre total is: $" + str(pretotal()))
            print(more())
            finished = True
        elif answer == 'n':
            pass
            finished = True
        else:
            print("Please enter 'y' for yes or 'n' for no.")

psum = float(sum(pizzas))

tax = round(decimal.Decimal(float(psum) * 0.13), 2)
final = round(decimal.Decimal(float(psum) * 1.13), 2)

print("Hello!")
print("Welcome to Pizza Code!")
print("Your pre total is: $" + str(pretotal()))
print(more())
print(remove())
print("Your final " + str(len(pizzas)) + " item(s) cost: ")
y = 0
for x in pizzas:
    y = y + 1
    print("   Item " + str(y) + "- $" + str(x))
print(psum)
print("Your tax is: $" + str(tax))
print("And your total is: $" + str(final))
print("Thank you for buying from Pizza Code!")
