def who_won(game_board: list):
    one = 0
    two = 0
    for item in game_board:
        for i in item:
            if i == 1:
                one += 1
            elif i == 2:
                two += 1
    if one > two:
        return 1
    elif two > one:
        return 2
    return 0


if __name__ == "__main__":
    game = [[1, 1, 2, 2], [2, 1, 1, 1], [0, 2, 1, 0]]
    print(who_won(game))
