# Write your solution here
number = int(input("Please type in a positive integer:"))

for item in range(-number, number + 1):
    if item == 0:
        continue
    print(item)
