# finding factorial
while True:
    number = int(input("Please type in a number:"))
    if number <= 0:
        print("Thanks and bye!")
        break
    store = number
    multi = 1
    while number > 0:
        multi *= number
        number -= 1
    print(f"The factorial of the number {store} is {multi}")
