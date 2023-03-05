N=int(input())
list=[]
for i in range(N):
    input_data=input().split()
    list.append((input_data[0],int(input_data[1])))


array1=list.sort(key=lambda x:x[1])
array2=sorted(list,key= lambda student:student[1])

