n = int(input())
num_list = list(map(int, input().split()))
final_list = []

for i in range(len(num_list)):
    initial = num_list[i]
    res_list = []
    res_list.append(initial)
    for j in (num_list[i+1:len(num_list)]):
        if(j > initial):
            res_list.append(j)
            initial = j
            
    final_list.append(res_list)

print(final_list)
print(len(max(final_list, key=len)))





