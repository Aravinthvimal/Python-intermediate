from itertools import combinations;

maths = int(input())
chem = int(input())
scince = int(input())
num = int(input())

def books(n, num):
    
    book_list = []

    num_list = list(range(n))
    comb = combinations(num_list, num)

    for i in list(comb):
        book_list.append(i)

    return len(book_list)
    
print(maths * books(chem,2) * books(scince, num))