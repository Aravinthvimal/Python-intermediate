row_count = int(input())
matrix = []
rep = []

for i in range(row_count):
    row = list(map(int, input().split()))
    matrix.append(row)

print(matrix)
col_count = len(matrix[0])

for i in range(row_count):
    for j in range(col_count - (col_count - 3)):
        if(matrix[i][j] == matrix[i][j] == matrix[i][j+1] == matrix[i][j+2] == matrix[i][j+3]):
            rep.append(matrix[i][j])

for i in range(row_count - (row_count - 2)):
    for j in range(col_count):
        if(matrix[i][j] == matrix[i][j] == matrix[i+1][j] == matrix[i+2][j] == matrix[i+3][j]):
            rep.append(matrix[i][j])

for i in range(row_count - (row_count - 2)):
    for j in range(col_count - (col_count - 3)):
        if(matrix[i][j] == matrix[i][j] == matrix[i+1][j+1] == matrix[i+2][j+2] == matrix[i+3][j+3]):
           rep.append(matrix[i][j])
        
if(len(rep) > 0):
    print(min(rep))
else:
    print("-1")
    