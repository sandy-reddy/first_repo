class CountCalls:

    def __init__ (self, func):
        self.func = func
        self.num_calls = 0


#call method allows you to exceute a object of this class, just like a funciton. 
# For eg if this method has a print function, and you create a class like cc = CountCalls(None), every time you execute (or call?) the object cc(), the print function like will run
    def __call__(self, *args, **kwargs):  
        self.num_calls += 1 
        print (f"This is excecuted {self.num_calls} times")
        return self.func(*args, **kwargs)



@CountCalls
def say_hello():
    print ("hello")


say_hello()
say_hello()

