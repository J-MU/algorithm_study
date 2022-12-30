def listToInt(arr):
    for i in arr:
        print(i,end="")

A,B=map(int,input().split())

A=list(map(int,str(A)))
B=list(map(int,str(B)))

A.reverse()
B.reverse()

for i in range(len(A)):
    if(A[i]>B[i]):
        listToInt(A)
        break
    elif(A[i]<B[i]):
        listToInt(B)
        break

print()

