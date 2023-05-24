import itertools

comb = itertools.permutations(range(1, 8))
for i in range(4467):
    next(comb)
print(next(comb))
