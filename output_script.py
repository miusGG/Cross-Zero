"""
Тут сделана функция по выводу получившегося результата
"""


def output_ans(pos, row, matrix, cross, zero):
    out_matrix = matrix  # передаем матрицу для дальнейшего ее изменения

    s = ""  # тут будет либо Х либо 0

    if cross:
        s = "X"
    if zero:
        s = "0"

    if row == 0 or row == 1 or row == 2:  # тут рассмотрим когда изменения произошли в 1 ряду, 2 ряду, 3 ряду и
        # поставим нужные символы в определнные места отталкиваясь от позиции переданной в функцию (pos)
        if row == 0:
            out_matrix[pos] = s
        elif row == 1:
            out_matrix[pos + 3] = s
        elif row == 2:
            out_matrix[pos + 6] = s
    elif row == 3 or row == 4 or row == 5:  # 1 2 3 столбцы
        if row == 3:
            if pos == 0:
                out_matrix[0] = s
            elif pos == 1:
                out_matrix[3] = s
            elif pos == 2:
                out_matrix[6] = s

        elif row == 4:
            if pos == 0:
                out_matrix[0 + 1] = s
            elif pos == 1:
                out_matrix[3 + 1] = s
            elif pos == 2:
                out_matrix[6 + 1] = s

        elif row == 5:
            if pos == 0:
                out_matrix[0 + 2] = s
            elif pos == 1:
                out_matrix[3 + 2] = s
            elif pos == 2:
                out_matrix[6 + 2] = s

    elif row == 6 or row == 7:  # 1 2 диагонали
        if row == 6:
            if pos == 0:
                out_matrix[0] = s
            elif pos == 1:
                out_matrix[4] = s
            elif pos == 2:
                out_matrix[8] = s
        elif row == 7:
            if pos == 0:
                out_matrix[2] = s
            elif pos == 1:
                out_matrix[4] = s
            elif pos == 2:
                out_matrix[6] = s

        # вывод ответа в нужном порядке
    print(out_matrix[0], out_matrix[1], out_matrix[2])
    print(out_matrix[3], out_matrix[4], out_matrix[5])
    print(out_matrix[6], out_matrix[7], out_matrix[8])
