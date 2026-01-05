number = int(input("Please type in a number:"))

top = 1
down = number

while top < down:
    print(top)
    print(down)
    top += 1
    down -= 1

if top == down:
    print(down)
