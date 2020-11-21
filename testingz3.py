def dig_pow(n, p):
    dig = list(str(n))
    sum = 0
    for ele in dig:
        sum += int(ele)**p
        p += 1
    if sum % n == 0:
        return sum / n
    else:  
        return -1


print(dig_pow(92, 1))

