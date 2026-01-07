def everything_reversed(array):
    new_array = []
    for item in array[::-1]:
        new_array.append(item[::-1])
    return new_array


if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
