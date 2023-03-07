print("Hello!")
name = input("Please give your name: ")
age = int(input("And age: "))
yes_no = input("Have you had your birthday this year yet? (yes or no): ")
year = 2023 - age
if yes_no == 'no':
    year = year-1
print("Hello " + name + "! You were born in: " + str(year))

