def longest_series_of_neighbours(array):
    index = 1
    neighbours = []
    temp = []
    while index < len(array):
        if abs(array[index] - array[index - 1]) == 1:
            neighbours.append(array[index - 1])
        else:
            neighbours = []
        index += 1
        if len(temp) <= len(neighbours):
            temp = neighbours
    return len(temp) + 1


if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))
