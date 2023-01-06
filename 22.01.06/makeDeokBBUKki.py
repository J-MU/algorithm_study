def binary_search(array,target,start,end):
    while start<=end:
        mid=(start+end)//2
        sum=find_sum(array,mid)
        if sum<target:
            end=mid-1
        elif sum>target:
            start=mid+1
        else:
            return mid
    return None

def find_sum(array,pivot):
    sum=0
    for i in array:
        if(i > pivot):
            e=i-pivot
        else:
            e=0
        sum+=e

    return sum
N,M=list(map(int,input().split()))

list=list(map(int,input().split()))

min=0
max=max(list)

H=binary_search(list,M,0,max)
print(H)