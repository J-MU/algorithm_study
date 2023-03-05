N=int(input())

arr=list(map(int,input().split()))

print(arr)
d=[0]*(N)

d[0]=arr[0]
d[1]=max(arr[0],arr[1])

for i in range(2,N):
    d[i]=max(d[i-1],d[i-2]+arr[i])

print(d)
print(d[N-1])
# 4
# 1 3 1 5