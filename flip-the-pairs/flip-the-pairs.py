number = int(input("Please type in a number:"))

count = 2
inner_count = 1
while count <= number:
    print(count)
    while True:
        print(inner_count)
        inner_count += 2
        break
    count += 2

if number % 2 != 0:
    print(inner_count)
