def palindromes(word):
    j = 1
    value = False
    for i in word:
        if i == word[len(word) - j]:
            value = True
        else:
            return False
        j += 1
    return value


while True:
    pali_word = input("Please type in a plaindrome: ")

    if palindromes(pali_word):
        print(f"{pali_word} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")
