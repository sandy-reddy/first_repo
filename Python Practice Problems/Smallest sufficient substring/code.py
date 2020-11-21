#Given an array of characters and a string, implement a function that finds the smallest substring containing all the characters in the array.

#input: abdacf  ,   a,b,c
# output: abdac




def substr(stri, letters):
#take letters and loop through them to find every single index they are located in stri. 
# Now how do we find the smallest continuious range in the group of numbers?
    for a in letters:
        if a in stri:
            print (stri.find(a))
        else:
            print ("no", a)



substr("abcdfsdfjkasdfhskjbc", "abc")




