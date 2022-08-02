# 이것이 코딩테스트다 -나동빈저자 (Chapter4 구현)
# p.100 상하좌우
from collections import deque

currentPosition=[1,1]
listLength=int(input())
directionList=deque(input().split())

def checkOutOfBounds(posX,posY):
    if(posX==0 or posX==6):
        return True # OutOfBounds
    elif(posY==0 or posY==6):
        return True # OutOfBounds
    else:
        return False # InBounds

def Uoperation(curDirection):
    if(checkOutOfBounds(curDirection[0]-1, curDirection[1])):   # OutOfBounds일때
        return 0;
    curDirection[0]+=1
    return 1;

def Doperation(curDirection):
    if(checkOutOfBounds(curDirection[0]+1, curDirection[1])):   # OutOfBounds일때
        return 0;
    curDirection[0]+=1
    return 1;

def Loperation(curDirection):
    if(checkOutOfBounds(curDirection[0], curDirection[1]-1)):   # OutOfBounds일때
        return 0;
    curDirection[1]-=1
    return 1;

def Roperation(curDirection):
    if(checkOutOfBounds(curDirection[0], curDirection[1]+1)):   # OutOfBounds일때
        return 0;
    curDirection[1]+=1
    return 1;


while(len(directionList)>0):
    curDirection=directionList.popleft()
    if(curDirection=="L"):
        Loperation(currentPosition)
    elif(curDirection=="R"):
        Roperation(currentPosition)
    elif(curDirection=="U"):
        Uoperation(currentPosition)
    elif(curDirection=="D"):
        Doperation(currentPosition)
    print(curDirection)
    print(currentPosition)


print(currentPosition)

