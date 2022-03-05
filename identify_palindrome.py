num = int(input())

def reverse_and_add(num):
    num = str(num)
    rev_num = int(num[::-1])
    return int(num) + rev_num

while(True):
    num = str(reverse_and_add(num))

    if(int(num) == int(num[::-1])):
        print(num)
        break
    