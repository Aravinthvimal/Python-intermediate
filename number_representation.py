num = int(input())

for i in range(2, 37):
    temp = num
    res = 0
    ctr = 0
    while(temp > 0):
        res += ((temp % i)*(10**ctr))  #Stacking remainders
        temp = int(temp / i)             #updating dividend
        ctr += 1

    res = str(res)
    res_len = len(res)

    if(res.count(res[0]) == res_len):
        print(res, i)
        