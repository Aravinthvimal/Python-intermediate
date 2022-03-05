from itertools import permutations

total = list(map(int, input().split(',')))
num = len(total) // 2
perm = list(permutations(total))
res = []

for i in list(perm):
    team_a = i[:num]
    team_b = i[num:]
    
    team_a_sum = sum(team_a)
    team_b_sum = sum(team_b)

    res.append([team_a_sum, team_b_sum, (max(team_a_sum, team_b_sum)-min(team_a_sum, team_b_sum))])

res.sort(key=lambda x:x[-1])

for i in (res[0][:-1]):
    print(i, end=" ")