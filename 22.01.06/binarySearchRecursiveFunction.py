def binary_search(array,target,start,end):
    mid=(start+end)//2

    if(start>end):
        return None;

    if(array[mid]>target):
        return binary_search(array,target,start,mid-1)
    elif(array[mid]<target):
        return binary_search(array,target,mid+1,end)
    else:
        return mid;


n, target=list(map(int,input().split()))
array=list(map(int,input().split()))

result=binary_search(array,target,0,n-1)

if result==None:
    print("원소가 없음!")
else:
    print(result+1,"번째 원소에 ",target,"이 있음!")

