def spruce(number):
    spaces = number - 1
    star = 1
    print("a spruce!")
    while spaces >= 0:
        print(f"{' ' * spaces}{'*' * star}")
        spaces -= 1
        star += 2
    print(f"{' ' * (number - 1)}{'*'}")


if __name__ == "__main__":
    spruce(5)
