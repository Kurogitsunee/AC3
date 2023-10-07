def is_same_color(k, l, m, n):
    return (k + l) % 2 == (m + n) % 2

def threatens_piece(piece, k, l, m, n):
    if piece == "ферзь":
        return k == m or l == n or abs(k - m) == abs(l - n)
    elif piece == "ладья":
        return k == m or l == n
    elif piece == "слон":
        return abs(k - m) == abs(l - n)
    elif piece == "конь":
        return (abs(k - m) == 2 and abs(l - n) == 1) or (abs(k - m) == 1 and abs(l - n) == 2)
    else:
        return False

def can_reach(k, l, m, n, piece):
    if piece == "ферзь" or piece == "ладья" or piece == "слон":
        if is_same_color(k, l, m, n) and not threatens_piece(piece, k, l, m, n):
            return "Нужно два хода."
        return "Можно одним ходом."
    else:
        if threatens_piece(piece, k, l, m, n):
            return "Можно одним ходом."
        elif is_same_color(k, l, m, n) and (abs(k - m) <= 4 or abs(l - n) <= 4) and abs(k - m) != 2  and abs(l - n) != 2:
            if ((abs(k - m) % 2 == 0) and (abs(l - n) % 2 == 0)) or ((abs(l - n) % 2 == 0) and (abs(k - m) % 2 == 0)) or ((abs(k - m) % 2 != 0) and (abs(l - n) % 2 != 0)) or ((abs(l - n) % 2 == 0) and (abs(k - m) % 2 == 0)):
                return "Нужно два хода."
        
def find_two_step_move(k, l, m, n, piece):
    for i in range(1, 9):
        for j in range(1, 9):
            if i != k or j != l:
                if threatens_piece(piece, k, l, i, j) and threatens_piece(piece, i, j, m, n) and can_reach(k, l, m, n, piece) == "Нужно два хода.":
                    return f"Первый ход: ({i}, {j}). Второй ход: ({m}, {n})."
    return "Нельзя достичь поля за 2 хода."
    
k = int(input("Введите вертикаль (k) для поля (k, l) (число от 1 до 8): "))
l = int(input("Введите горизонталь (l) для поля (k, l) (число от 1 до 8): "))
m = int(input("Введите вертикаль (m) для поля (m, n) (число от 1 до 8): "))
n = int(input("Введите горизонталь (n) для поля (m, n) (число от 1 до 8): "))
piece = input("Введите наименование фигуры (ферзь, ладья, слон или конь): ")

if (k == 0 or k > 8) or (l == 0 or l > 8) or (m == 0 or m > 8) or (n == 0 or n > 8):
    print("Ошибка ввода: одно (или оба) из указанных полей не существует.")
elif piece not in ["ферзь", "ладья", "слон", "конь"]:
    print("Ошибка ввода: неизвестная фигура.")
else:
    if is_same_color(k, l, m, n):
        print("Поля (k, l) и (m, n) одного цвета.")
    else:
        print("Поля (k, l) и (m, n) разного цвета.")

    if threatens_piece(piece, k, l, m, n):
        print(f"{piece.capitalize()} угрожает полю (m, n).")
    else:
        print(f"{piece.capitalize()} не угрожает полю (m, n).")

    if can_reach(k, l, m, n, piece) == "Можно одним ходом.":
        reachable = can_reach(k, l, m, n, piece)
        print(reachable)
    else:
        reachable = find_two_step_move(k, l, m, n, piece)
        print(reachable)
