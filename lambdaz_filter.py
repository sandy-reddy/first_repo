# filter(func, seq)

a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x%2==0, a)
print(list(b))

# c = [x for in a if x%2 == 0]
