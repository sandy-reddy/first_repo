#can do the same thing with a list if you switch out the () for []
import sys

mygenerator = (i for i in range(1000000) if i % 2 == 0)
# for i in mygenerator:
#     print(i)



mylist = [i for i in range(1000000) if i % 2 == 0]
# for i in mylist:
#     print(i)

print(sys.getsizeof(mygenerator))
print(sys.getsizeof(mylist))

