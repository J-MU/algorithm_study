N,M=map(int,input().split())

arr=[]

for i in range(N):
    arr.append(list(map(int,input().split())))
    arr[i].sort()

min_arr=[]

for i in range(N):
    min_arr.append(arr[i][0])

print(min_arr)

print(max(min_arr))


