#https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html


import random


# # Password generator


# char_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?"
password = ""


def weak_password():
    #parse 1000 password list until specified length password is returned
    # choose randint, go to specified line, choose randlen, if line lenght == randlen, print else repeat
    with open("Python Practice Problems/passwords.txt", "r") as fp:
        
        fp_gen = random.randint(1,1000)
        for line, value in enumerate(fp):
            
            if fp_gen == line:
                print(value)
                break
            else:
                continue
            

weak_password()



    

# def strong_password():
    #generate random char for specified length
    # return random char from char_list for specified length 

    





# while True:

#     usr= input("Password Generator: Type '1' for random strong password \n -------------------Type '2' for random weak password")



#     if usr == "1" or usr == "2":

#         break

#     else:
        
#             usr= input("Password Generator: Type '1' for random strong password \n -------------------Type '2' for random weak password")
    
    











