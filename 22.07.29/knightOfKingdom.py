# 이것이 코딩테스트다 -나동빈저자 (Chapter4 구현)
# p.115 숫자 카드 게임

curpostion=list(input())
print(curpostion)

if(curpostion[0]=='a'):
    curpostion[0]=1
elif(curpostion[0]=='b'):
    curpostion[0] = 2
elif(curpostion[0]=='c'):
    curpostion[0] = 3
elif(curpostion[0]=='d'):
    curpostion[0] = 4
elif(curpostion[0]=='e'):
    curpostion[0] = 5
elif(curpostion[0]=='f'):
    curpostion[0] = 6
elif(curpostion[0]=='g'):
    curpostion[0] = 7
elif(curpostion[0]=='h'):
    curpostion[0] = 8

def checkOutOfBounds(posX,posY):
    if(posX<=0 or posX>=9):
        return 1;
    elif(posY<=0 or posY>=9):
        return 1
    else:
        return 0

posX,posY=list(map(int,curpostion))

count=0
if(not checkOutOfBounds(posX-1,posY+2)): #not out of bounds
    count+=1
if(not checkOutOfBounds(posX+1,posY+2)): #not out of bounds
    count+=1
if(not checkOutOfBounds(posX+2,posY+1)): #not out of bounds
    count+=1
if(not checkOutOfBounds(posX+2,posY-1)): #not out of bounds
    count+=1
if(not checkOutOfBounds(posX-1,posY-2)): #not out of bounds
    count+=1
if(not checkOutOfBounds(posX+1,posY-2)): #not out of bounds
    count+=1
if(not checkOutOfBounds(posX-2,posY+1)): #not out of bounds
    count+=1
if(not checkOutOfBounds(posX-2,posY-1)): #not out of bounds
    count+=1

print(curpostion)
print(count)
