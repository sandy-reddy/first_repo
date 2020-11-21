# collections: Counter, namedtuple, OrderedDict, defaultdict, deque

# from collections import Counter

# a = "aaaaaaaabbbbccc"

# my_counter = Counter(a) 
#returns a dictionary with keys and values based on count of elements
#print (my_counter) #can also use print methods .keys() or .values() 

#>>> Counter({'a': 8, 'b': 4, 'c': 3})

# print(my_counter.most_common(1)[0][0])
#accessing the most common (1st arg) as a tuple then accessing the first tuple (2nd arg) and then the first element inside that tuple (3rd arg)

# from collections import namedtuple

# creates a class with the feilds x and y
# Point = namedtuple("Point", "x,y")

# pt = Point(1, -4)
# print(pt.x, pt.y)
# >>> 1 -4

# from collections import defaultdict
#a dictionary with defualt values

# d = defaultdict(int) #allows you to choose a defualt value type

# d["a"] = 1
# d["b"] = 2
#int> 0
#float> 0.0
#list > []

# print(f" {d['a']} and {d['b']} and {d['c']} yay no error")

from collections import deque
# a double ended queue

d = deque()

d.append(1)
d.append(2)
print(d)

d.appendleft(3) #appends to the left side
print(d)

d.pop() #remove rightmost value
# d.popleft remove leftmost value
# d.extend(), d.clear()
d.extendleft([4, 5, 6])
print(d)

d.rotate(1) #moves all elements 1 place to the right
print(d)



