H,M=map(int,input().split())
if(M<45):
    M=M+15
    H=(H-1)%24
else:
    M-=45

print(H,M)