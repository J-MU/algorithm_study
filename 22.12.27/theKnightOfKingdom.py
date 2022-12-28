movableX=[-2,-2,-1,1,2,2,1,-1]
movableY=[1,-1,-2,-2,1,-1,2,2]

list=list(input())
X=ord(list[0])-97
Y=int(list[1])-1
print(X,Y)

count=0

for i in range(len(movableY)):
    newX=X+movableX[i]
    newY=Y+movableY[i]
    if(newX>=0 and newX<8 and newY>=0 and newY<8):
        count=count+1

print(count)