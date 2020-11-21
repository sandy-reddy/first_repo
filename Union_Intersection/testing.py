odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}


u = odds.union(evens)
print(u)

i = odds.intersection(primes)
print(i)

print(setA.difference(setB))
print(setB.difference(setA))

print(setB.symmetric_difference(setA))

print(setA.update(setB))
print(setA)

setA.intersection_update(setB) #updates setA with what is found in both sets
print(setA)

setA.difference_update(setB)
print(setA)

print(setB)
setA.symmetric_difference_update(setB)
print(setA)
