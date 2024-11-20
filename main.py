from output_script import output_ans

'''
Вввод:
Определяем наше игровое поле (матрицу)
Вводим ее и переаодим в удобный вид
Далее определяем за кого нужно сделать ход (Крестик\нолик)

Так же разделим наше игровое поле на:
1 2 3 ряды
1 2 3 столбцы
1 и 2 диагонали
все их я записал в массив all
'''

matrix_size = (3, 3)
matrix = []
for i in range(matrix_size[0]):
    temp = input()
    matrix += temp.split(" ")

CROSS = False
ZERO = False
cross_or_zero = int(input("За кого вы хотите чтобы программа сделала ход? \n1 - Крестики\n0 - Нолики\n>>> "))
if cross_or_zero == 1:
    CROSS = True
    s = 'X'

elif cross_or_zero == 0:
    ZERO = True
    s = '0'

else:
    print("Error input ;(\n!Ошибка ввода. Перезапустите программу.")

row1 = [matrix[0], matrix[1], matrix[2]]
row2 = [matrix[3], matrix[4], matrix[5]]
row3 = [matrix[6], matrix[7], matrix[8]]
colum1 = [matrix[0], matrix[3], matrix[6]]
colum2 = [matrix[1], matrix[4], matrix[7]]
colum3 = [matrix[2], matrix[5], matrix[8]]
diagonal1 = [matrix[0], matrix[4], matrix[8]]
diagonal2 = [matrix[2], matrix[4], matrix[6]]

all = (row1, row2, row3, colum1, colum2, colum3, diagonal1, diagonal2)
answer = -1
i_elem = -1

'''
Алгоритм:
Есть два алгоритма для крастиков и для ноликов, но работают они идентично:
Обусловимся что играем мы за X
    Сначала проверяем есть ли 2 крестика в ряду\столбце\диагонали
        Если есть ставим и заканчиваем проверку
    Если нет то смотрим есть ли 2 нолика в ряду\столбце\диагонали
        Если есть то ставим 3им Х
    Если нет то смотрим есть ли 1 Х на ряду\столбце\диагонали
        Если если есть то ставим куда то рядом дургой крестик
    Если итогу скрипта не было найдено место для Х, то ставиться в первое попавшееся пустое место
    
    Далее идет функция вывода ответа, она находиться в отдельном файле и пояснения к ней там же!
'''

if CROSS:
    for i in range(len(all)):
        mass = all[i]
        if "X" in mass:
            if mass[0] == "X" and mass[1] == "X" and mass[2] != "0":
                answer = 2
                i_elem = i
                break
            elif mass[2] == "X" and mass[1] == "X" and mass[0] != "0":
                answer = 0
                i_elem = i
                break
            elif mass[0] == "X" and mass[2] == "X" and mass[1] != "0":
                answer = 1
                i_elem = i

                break
        elif "0" in mass and answer == -1:
            if mass[0] == "0" and mass[1] == "0" and mass[2] != "X":
                answer = 2
                i_elem = i
            elif mass[2] == "0" and mass[1] == "0" and mass[0] != "X":
                answer = 0
                i_elem = i
            elif mass[0] == "0" and mass[2] == "0" and mass[1] != "X":
                answer = 1
                i_elem = i

    if answer == -1:
        for i in range(len(all)):
            mass = all[i]
            if "X" in mass:
                if mass[0] == "_" and mass[1] == "_":
                    answer = 0
                    i_elem = i
                elif mass[2] == "_" and mass[1] == "_":
                    answer = 2
                    i_elem = i
                elif mass[0] == "_" and mass[2] == "_":
                    answer = 0
                    i_elem = i

if ZERO:
    for i in range(len(all)):
        mass = all[i]
        if "0" in mass:
            if mass[0] == "0" and mass[1] == "0" and mass[2] != "X":
                answer = 2
                i_elem = i
                break
            elif mass[2] == "0" and mass[1] == "0" and mass[0] != "X":
                answer = 0
                i_elem = i
                break
            elif mass[0] == "0" and mass[2] == "0" and mass[1] != "X":
                answer = 1
                i_elem = i
                break
        elif "X" in mass and answer == -1:
            if mass[0] == "X" and mass[1] == "X" and mass[2] != "0":
                answer = 2
                i_elem = i
            elif mass[2] == "X" and mass[1] == "X" and mass[0] != "0":
                answer = 0
                i_elem = i
            elif mass[0] == "X" and mass[2] == "X" and mass[1] != "0":
                answer = 1
                i_elem = i

    if answer == -1:
        for i in range(len(all)):
            mass = all[i]
            if "0" in mass:
                if mass[0] == "_" and mass[1] == "_":
                    answer = 0
                    i_elem = i
                elif mass[2] == "_" and mass[1] == "_":
                    answer = 2
                    i_elem = i
                elif mass[0] == "_" and mass[2] == "_":
                    answer = 0
                    i_elem = i

'''
answer Это на каком месте будет стоят крестик или нолик в all[i_elem] от 0 до 2 (3 элемента)
i_elem Это от 0 до 7 по массиву all
'''
if answer == -1:
    for i in range(len(matrix)):
        if matrix[i] == "_":
            matrix[i] = s
            break

output_ans(answer, i_elem, matrix, CROSS, ZERO)
