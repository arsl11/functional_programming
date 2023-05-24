with open('seq2.txt', 'r') as file:
    n = file.readline().strip('\n')
    n = int(n)
    f_seq = []
    while len(f_seq) < n:
        f_seq += file.readline().strip('\n').split(" ")

    m = file.readline().strip('\n')
    m = int(m)
    s_seq = []
    while len(s_seq) < n:
        s_seq += file.readline().strip('\n').split(" ")

# Функция для нахождения наибольшей общей последовательности
def longest_common_sequence(seq1, seq2):

    len1, len2 = len(seq1), len(seq2)

    # Создаем матрицу, чтобы хранить значения для динамического программирования
    dp_table = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    # Заполняем матрицу
    for i in range(len1):
        for j in range(len2):
            if seq1[i] == seq2[j]:
                dp_table[i + 1][j + 1] = dp_table[i][j] + 1
            else:
                dp_table[i + 1][j + 1] = max(dp_table[i][j + 1], dp_table[i + 1][j])

    # Получаем длину наибольшей общей последовательности
    lcs_length = dp_table[len1][len2]

    # Получаем саму наибольшую общую последовательность
    lcs = ''
    i, j = len1, len2
    while i > 0 and j > 0:
        if dp_table[i][j] == dp_table[i - 1][j]:
            i -= 1
        elif dp_table[i][j] == dp_table[i][j - 1]:
            j -= 1
        else:
            assert seq1[i - 1] == seq2[j - 1]
            lcs = seq1[i - 1] + lcs
            i -= 1
            j -= 1

    return lcs_length

print(longest_common_sequence(f_seq, s_seq))


# функция для перебора правильных скобочных последовательностей с двумя типами скобок