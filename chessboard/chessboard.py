def chessboard(arg1):
    count = 1
    outer = arg1
    while outer > 0:
        inner_arg = arg1
        while inner_arg > 0:
            print(count, end="")
            if count == 0:
                count += 1
            else:
                count -= 1
            inner_arg -= 1

        if arg1 % 2 == 0:
            if count == 0:
                count += 1
            else:
                count -= 1
        outer -= 1
        print()


# Testing the function
if __name__ == "__main__":
    chessboard(4)
