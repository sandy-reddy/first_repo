#  %, .format{}, f-strings

var = "Tom"

# %
my_string = "the varibale is %s" %var  
# %d used for int number, %f for float 
#print(my_string)
#>>> the varibale is Tom

#.format()
my_string = "the varibale is {}".format(var)
#print(my_string)
#>>> the varibale is Tom

# f-string
my_string = f"the varibale is {var}" #can also use opperations inside brackets 
#print(my_string)
#>>> the varibale is Tom

