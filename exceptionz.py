# x = -5

# assert(x>=0), "x not pos value"

# try:
#     a = 5/0
# except:
#     print("an error happened")

# # can also catch the specific error by specifiying it in the except statement

# try:
#     a = 5/0
# except ZeroDivisionError:
#     print("zerodiverror")

# #can also catch unspecified error by using e as a generic error but its good practice to catch specific error

# try:
#     a = 5/0
# except Exception as e:
#     print(e)

# #multiple exceptions, will return first exception

# try:
#     a = 5/0 
#     b = 1 +"1"
# except ZeroDivisionError:
#     print("zero division")
# except TypeError:
#     print("adding string to int")
# else:
#     print("your good")
# finally:   #always runs, most commonly used to clean up
#     print("cleaning up...")

class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x>100:
        raise ValueTooHighError("value is too high")
    if x<5:
        raise ValueTooSmallError("value is too small", x)


try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)




