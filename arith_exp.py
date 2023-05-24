import itertools

# Создаем список из символов "+-" длиной 9
symbols = ["+", "-"]
seq_length = 9
sequences = list(itertools.product(symbols, repeat=seq_length))


numbers = [21, 27, 34, 20, 29, 24, 38, 38, 22, 24]

ans = 21

for i in range(len(sequences)):
    for j in range (len(sequences[i])):
        if sequences[i][j] == "+":
            ans += numbers[j + 1]
        if sequences[i][j] == "-":
            ans -= numbers[j + 1]
    print(ans)
    if ans == 25:
        print(sequences[i])
        break        
    else: 
        ans = 21
        
    
