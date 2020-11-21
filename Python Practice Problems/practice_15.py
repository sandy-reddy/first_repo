# https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html



#write a program to reverse order of a stentence 




def reverse(string):
    #init final list
    rev_string = []
    #sep initial string
    sep_string = string.split()
    for w in sep_string:
         rev_string.append((sep_string[(len(sep_string)) - (sep_string.index(w)+1)]))
    print(rev_string)

a = "hi my name is sandeep"

reverse(a)
# input("type a sentence\n")



######## one line solution###########

# def reverseWord(w):
#   return ' '.join(w.split()[::-1])

