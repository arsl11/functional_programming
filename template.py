s = "?be?bdcb?dcb?debcd??bdad?ee"
n = 5151

def to_5_system(n, length):
    digits = "abcde"
    res = ""
    while n > 0:
        res = digits[n%5] + res
        n //= 5
    return "a" * (length - len(res)) + res   # дополнить "нулями"
    

replacement = to_5_system(n-1, s.count("?") )

i = 0
res = "" 

for letter in s:
    if letter == '?':
        res += replacement[i]
        i += 1
    else:
        res += letter
        
print(res)