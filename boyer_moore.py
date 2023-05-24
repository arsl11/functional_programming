def boyer_moore(pattern, text):
    # Создаем таблицу смещений
    table = {}
    for i in range(len(pattern)):
        table[pattern[i]] = max(1, len(pattern) - i - 1)

    # Начинаем поиск
    i = len(pattern) - 1
    while i < len(text):
        j = len(pattern) - 1
        while text[i] == pattern[j]:
            if j == 0:
                return i
            i -= 1
            j -= 1
        i += table.get(text[i], len(pattern))
    return -1

pattern = "cd"
text = "abcbcbdcbbcbdcbbcd"

index = boyer_moore(pattern, text)
print(index)
