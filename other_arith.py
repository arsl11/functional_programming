def find_signs(n, x, nums):
    pl = 1 << (n-1)  # первый знак уже +
    print(pl)

    while pl < (1 << n):  
        res = 0
        for i in range(n):
            if pl & (1 << (n-i-1)):
                res += nums[i]
            else:
                res -= nums[i]
        if res == x:
            return pl
        else:
            pl += 1
            
def print_with_signs(n, x, nums):
    res = ""
    sigs = find_signs(n, x, nums)
    print(bin(sigs))
    for i in range(n) :
        if sigs & (1 << (n-i-1)):
            res += f"+{nums[i]}"
        else:
            res += f"-{nums[i]}"
    return res[1:]

numbers = []
with open("arithm2.txt", "r") as file:
    n, x = map(int, file.readline().split())
    numbers = file.readline().split(" ")
    numbers = [int(num) for num in numbers]

print(print_with_signs(n, x, numbers))