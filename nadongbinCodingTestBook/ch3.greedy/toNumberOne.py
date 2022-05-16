N,K=list(map(int,input().split()))
print(N,K)

remainer=N%K
print(remainer)
multiple_number=N-remainer
cnt=0
while True:
    print(multiple_number,cnt)
    if(multiple_number==1):
        print('cnt:',cnt)
        break
    multiple_number=multiple_number//K
    cnt+=1

print(remainer+cnt)