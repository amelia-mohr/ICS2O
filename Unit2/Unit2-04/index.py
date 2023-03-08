for numbers in range(1,33): 
    if numbers % 15 == 0.0:
        print(str(numbers) + " FizzBuzz")
    elif numbers % 3 == 0.0:
        print(str(numbers) + " Fizz")
    elif numbers % 5 == 0.0:
        print(str(numbers) + " Buzz")
    else:
        print(numbers)
    