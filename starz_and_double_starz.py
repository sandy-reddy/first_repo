#multiplication operation
mult = 2*4
print (mult)  

#power operation
power = 2 ** 4
print(power)

#list/tuple/str duplication operation
zero = [1, 5] * 10
print(zero)

#* args and **kwargs
def somefunc(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for k in kwargs:
        print(k , kwargs[k])

somefunc("a", "b", "c", "d", "e", six="f", seven="g")


###unpacking stuff, ** for dictionary
def doo(a, b, c):
    print(a, b, c)

some_list= [1, 2, 3]
doo(*some_list)

#more unpacking, will always unpack into list

nums = [1, 2, 3, 4, 5, 6, 7, 8]

*beginning_cannamethisanything, last_cannamethisanything = nums 

print(beginning_cannamethisanything)
print(last_cannamethisanything)

#to pack, can also pack dictionaries if you use **

a_list = [1, 2, 3]
a_tuple = (4, 5, 6)
a_set = {5, 6, 7, 8, 9, 9, 9, 9, 9, 9}

a_nums = (*a_list, *a_tuple, *a_set)
print(*a_list, *a_tuple, *a_set)
print(a_nums)



