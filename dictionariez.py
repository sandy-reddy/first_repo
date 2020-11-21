some_string = "Hi, hello how are you doing. My name is Sandeep Siddapureddy. Some people call me Sandy or Deep. I don't rly care what you call me."

count = {}

for char in some_string:
    count.setdefault(char, 0)
    count[char] = count[char] + 1

for k, v in count.items():
    print(k,v)



# a = count.keys()
# print(a)





