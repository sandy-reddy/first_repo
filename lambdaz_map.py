#lambda arguments: expression
#map(func, seq)

a = [1, 2, 3, 4, 5]
b = map(lambda x: x+2, a)
print(list(b))

#above is the same thing as using list comp 
# c = [x + 2 for x in a]





