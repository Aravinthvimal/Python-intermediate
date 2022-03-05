m, num = input().split()
num_array = list(map(int, input().split()))
count = 0

num_array.sort()

for i in range(len(num_array)-2):
    num = num_array[i]
    num2 = num + 1
    num3 = num + 2

    if(num2 in num_array and num3 in num_array):
        count += 1
        num_array[i] = 0
        num_array[num_array.index(num2)] = 0
        num_array[num_array.index(num3)] = 0

for i in range(len(num_array)-2):

    num = num_array[i]
    num2 = num_array[i+1]
    num3 = num_array[i+2]

    if(num_array[i] != 0):
        if(num == num2 == num3 ):
            count += 1
            num_array[i] = 0
            num_array[i+1] = 0
            num_array[i+2] = 0
            
print(count)
