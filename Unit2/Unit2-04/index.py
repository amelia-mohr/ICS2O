for numbers in range(1,33): 
    if numbers % 15 == 0.0:
        print("FizzBuzz")
    elif numbers % 3 == 0.0:
        print("Fizz")
    elif numbers % 5 == 0.0:
        print("Buzz")
    else:
        print(numbers)
    