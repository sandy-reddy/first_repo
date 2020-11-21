import sys


def sum_of_num_gen(n):
    num = 0
    while n>0:
        yield n
        num = num + n 
        n -= 1

    

   
def sum_of_num_list (nu):
    count = nu
    listed = []
    while count > 0:
        listed.append(count)
        count -=1
    return listed

print (sum(sum_of_num_list(10000000)))

print (sum(sum_of_num_gen(10000000)))

print(sys.getsizeof(sum_of_num_list(10000000)))

print(sys.getsizeof(sum_of_num_gen(10000000)))





