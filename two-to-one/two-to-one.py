# Write your solution here
def longest(a1, a2):
    a1 = sorted(list(a1))
    a2 = sorted(list(a2))
    i = 0
    j = 0
    new_string = ""
    while j < len(a2) and i < len(a1):
        if a1[i] == a2[j]:
            if a1[i] not in new_string:
                new_string += a1[i]
            i += 1
            j += 1
        elif a1[i] > a2[j] and a2[j] not in new_string:
            new_string += a2[j]
            j += 1
        elif a2[j] > a1[i] and a1[i] not in new_string:
            new_string += a1[i]
            i += 1
        elif a1[i] in new_string:
            i += 1
        elif a2[j] in new_string:
            j += 1

    while j < len(a2):
        if a2[j] not in new_string:
            new_string += a2[j]
        j += 1
    while i < len(a1):
        if a1[i] not in new_string:
            new_string += a1[i]
        i += 1
    return new_string


a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
print(longest(a, b))
