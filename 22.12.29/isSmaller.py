N,X=map(int,input().split())
int_arr=list(map(int,input().split()))
answer=[]
for i in range(N):
    if(int_arr[i]<X):
        answer.append(str(int_arr[i]))

str=" ".join(answer)
print(str)