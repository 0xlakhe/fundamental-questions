def squared(string, number):
    outer_count = 0
    index = 0
    while outer_count < number:
        string_count = number
        while string_count > 0:
            print(string[index], end="")
            index += 1
            if index == len(string):
                index = 0
            string_count -= 1
        print()
        outer_count += 1


if __name__ == "__main__":
    squared("aybabtu", 5)
