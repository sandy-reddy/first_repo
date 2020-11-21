# Write a Python program to find unique triplets whose three elements gives the sum of zero from an array of n integers.

# Find the lowest number in the list, try and find 2 other positive numbers that equal the negative 



from itertools import combinations

arr = [-4, -3, -2, -1, 0, 1, 2 , 3, 4]

combs = combinations(arr, 3)

# print (list(combs))

for x, y, z in list(combs):
    if x + y + z == 0:
        print (x, y, z)








