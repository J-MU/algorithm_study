def binary_search(array,target,start,end):
    while start<=end:
        mid=(start+end)//2

        if(array[mid]<target):
            start=mid+1
        elif array[mid]>target:
            end=mid-1
        else:
            return mid
    return None


N=int(input())
shop_array=list(map(int,input().split()))
shop_array.sort()

M=int(input())
buy_array=list(map(int,input().split()))

print(shop_array)
print(buy_array)

for i in range(M):
    if(binary_search(shop_array,buy_array[i],0,N-1)==None):
        print("no",end=" ")
    else:
        print("yes", end=" ")


