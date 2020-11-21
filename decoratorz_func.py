


# print_name = start_end_decorator(print_name) is the same thing as the @start_end_decorator statement below

# @start_end_decorator
# def print_name():
#     print("Alex")

# print_name()


#what happens if your function has an argument?...

import functools

# def start_end_decorator(func):

#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print("start")
#         result = func(*args, **kwargs)
#         print("end")
#         return result
#     return wrapper

# @start_end_decorator
# def add5 (x):
#     return x+5

# print(help(add5))
# print(add5.__name__)
 

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range (num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=4)
def greet(name):
    print(f"hello {name}")


greet("sandeep")

print(help(greet))
print(greet.__name__)


