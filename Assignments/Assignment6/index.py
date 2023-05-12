def calc(num):
    x = 1
    z = 1
    pi = 0
    for y in range(1, int(num) + 1):
        pi = pi + (z / x)
        x = x + 2
        z = z * -1
    return pi * 4

finished = False
while not finished: 
    print("To exit type 'q'")
    it = input("Please enter a number of iterations for pi: ")
    try:
        int(it)
    except ValueError:
        if it == 'q':
            finished = True
        else: 
            print("Please enter a NUMBER!")
    else: 
        if int(it) < 0:
            print("Please enter a POSITIVE number!")
        else: 
            print("The value of pi with " + str(it) + " iterations is: " + str(calc(it)))
