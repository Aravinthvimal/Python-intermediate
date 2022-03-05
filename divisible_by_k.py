from itertools import permutations

base = int(input())
div = int(input())
num = input()
count = 0

perm = permutations(num)

for i in list(perm):
    a = ''.join(i)
    aa = int(a,base)
    
    if(aa %div == 0):
        count += 1

print(count)