def same_chars(word, index_1, index_2):
    if index_1 >= len(word) or index_2 >= len(word) or word[index_1] != word[index_2]:
        return False
    else:
        return True


if __name__ == "__main__":
    print(same_chars("coderc", 1, 10))
