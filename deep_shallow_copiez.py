import copy

org = [1, 2, 3, 4, 5, 6, 7]

# cpy = copy.copy(org)
# cpy = list(org)
cpy = org[:]

cpy[0] = -10
print (org)
print(cpy)

#this is all shallow, see what happens when you try and go more than "one level" deep.

org = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12]]
cpy = copy.copy(org)   #must use copy.deepcopy()

cpy[0][0] = 0

print (org)
print (cpy)

#both lists get effected


