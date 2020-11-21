# from itertools import product

# a = [1, 2]
# b = [3]

# prod = product (a, b, repeat = 2)
# print(list(prod))
# prod = product (a, b, repeat = 1)
# print(list(prod))


# from itertools import permutations

# a = [1, 2, 3]

# prem = permutations(a)
# print(list(prem))

# prem = permutations(a,2 )
# print(list(prem))

from itertools import combinations, combinations_with_replacement

a = [1, 2, 3]

comb = combinations(a,3)
print(list(comb))

comb = combinations(a, 2)
print(list(comb))

comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))


