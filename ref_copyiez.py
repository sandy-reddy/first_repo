org = 5
cpy = org

#there is a copy at this point, not a reference 
#now when org is reassigned, cpy still holds the old same value in memory so it doesnt change
org = 6
print(org, cpy)


#this works differenty with mutable data types
#in this case, a reference is made. In other words cpy still references org whenever cpy is called and visa versa
#so a change to either will effect both
org = [1, 2, 3, 4, 5, 6]
cpy = org
org[0] = 0
cpy[0] = -1
print (org)
print(cpy)


