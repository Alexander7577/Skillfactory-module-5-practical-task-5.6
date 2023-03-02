import random


def Hello():
    print("Добро пожаловать в игру 'крестики-нолики'")
    print("========================================")


def ShowField():
    print("  | 0 | 1 | 2 |")
    print("--|-----------|")
    for i in range(3):
        print(f"{i} | {field[i][0]} | {field[i][1]} | {field[i][2]} |")
        print("--|-----------|")


def step():
    while True:
        try:
            x = int(input("Введите номер строки: "))
            y = int(input("Введите номер столбца: "))

        except:
            print("Введите целое число!")
            continue

        if x > 2 or y > 2:
            print("Вы ввели слишком большие значения=(")
            continue

        if field[x][y] != " ":
            print("Эта клетка уже занята, выберите другую.")
            continue

        return x, y


def winner():
    win_step = [[field[0][0], field[1][0], field[2][0]], [field[0][1], field[1][1], field[2][1]],
                [field[0][2], field[1][2], field[2][2]], [field[0][0], field[1][1], field[2][2]],
                [field[0][2], field[1][1], field[2][0]]]
    for i in range(3):
        if field[i] == ['X', 'X', 'X']:
            print("Крестики победили!!!")
            return True

    for i in range(5):
        if win_step[i] == ['X', 'X', 'X']:
            print("Крестики победили!!!")
            return True

    for i in range(3):
        if field[i] == ['0', '0', '0']:
            print("Нолики победили!!!")
            return True

    for i in range(5):
        if win_step[i] == ['0', '0', '0']:
            print("Нолики победили!!!")
            return True

    return False


Hello()
field = [[" "] * 3 for i in range(3)]
rand = random.randint(0, 1)
print("Удача на стороне ноликов, они ходят первые!" if rand == 0 else "Удача на стороне крестиков, они ходят первые!")
print("========================================")
for i in range(9):
    ShowField()
    print("========================================")
    x, y = step()
    print("========================================")
    if rand % 2 == 0:
        field[x][y] = "0"

    elif rand % 2 == 1:
        field[x][y] = "X"

    if winner():
        break
    rand += 1

    if i == 8:
        print("У вас дружеская ничья!")
