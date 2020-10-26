def create_gamefield():
    gamefield = [''] * 3
    for i in range(len(gamefield)):
        gamefield[i] = ['_'] * 3
    return gamefield


def print_gamefield(gamefield):
    for i in range(3):
        for j in range(3):
            print(gamefield[i][j] + ' ', end='')
        print()


def place_input(index, gamefield, input):
    row = index / 3
    column = (index - 1) % 3
    if row <= 1:
        gamefield[0][column] = input
    elif row > 1 and row <= 2:
        gamefield[1][column] = input
    elif row > 2 and row <= 3:
        gamefield[2][column] = input


def check_if_win(gamefield):
    counter = 0
    counter2 = 0
    for i in range(3):
        for j in range(3):
            if gamefield[i][j] == 'x':
                counter += 1
            if gamefield[i][j] == 'o':
                counter2 += 1
        if counter == 3 or counter2 == 3:
            return True
        counter = 0
        counter2 = 0

    for i in range(3):
        for j in range(3):
            if gamefield[j][i] == 'x':
                counter += 1
            if gamefield[j][i] == 'o':
                counter2 += 1
        if counter == 3 or counter2 == 3:
            return True
        counter = 0
        counter2 = 0

    if gamefield[0][0] == 'x' and gamefield[1][1] == 'x' and gamefield[2][2] == 'x':
        return True

    if gamefield[0][2] == 'x' and gamefield[1][1] == 'x' and gamefield[2][0] == 'x':
        return True

    if gamefield[0][0] == 'o' and gamefield[1][1] == 'o' and gamefield[2][2] == 'o':
        return True

    if gamefield[0][2] == 'o' and gamefield[1][1] == 'o' and gamefield[2][0] == 'o':
        return True

    return False


def check_if_gamefield_is_filled(gamefield):
    counter = 0
    for i in range(3):
        for j in range(3):
            if gamefield[i][j] == 'x' or gamefield[i][j] == 'o':
                counter += 1

    if counter == 9:
        return True

    return False


gamefield = create_gamefield()

while not check_if_gamefield_is_filled(gamefield):
    print_gamefield(gamefield)
    user1 = int(input('Eingabe Spieler 1:'))
    place_input(user1, gamefield, 'x')
    if check_if_win(gamefield):
        print('Spieler 1 wins!')
        break

    if check_if_gamefield_is_filled(gamefield):
        break

    print_gamefield(gamefield)
    user2 = int(input('Eingabe Spieler 2:'))
    place_input(user2, gamefield, 'o')
    if check_if_win(gamefield):
        print('Spieler 2 wins!')
        break
