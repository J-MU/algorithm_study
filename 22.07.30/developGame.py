# 이것이 코딩테스트다 -나동빈저자 (Chapter3 그리디)
# p.92 큰수의 법칙
# 출처: 2019 국가 교육기관 코딩 테스트
# 07.29~07.30
def checkLeftSide(nextStep,curPosition):
    nextPosition=[curPosition.posX+nextStep[1],curPosition.posY+nextStep[0]]
    if gameMap[nextPosition[1]][nextPosition[0]]==1:
        return False
    else:
        prevPosition.posX=curPosition.posX
        prevPosition.posY=curPosition.posY
        curPosition.posX=nextPosition[1]
        curPosition.posY=nextPosition[0]
        return True

def checkCanGoInit(checkCanGo):
    for i in range(len(checkCanGo)):
        checkCanGo[i]=0

def nextSight(curSightIndex):
    if curSightIndex+1==4:
        return True
    else:
        return False

class position:
    posX=0
    posY=0

    def __str__(self):
        return f'[{self.posX},{self.posY}]'

row,col=map(int,input().split())
curPosition=position()
curPosition.posX,curPosition.posY,sight=map(int,input().split())
prevPosition=position()

gameMap=list()

sightDirection=[0,3,2,1] #북 서 남 동
direction=[(0,-1),(1,0),(0,1),(-1,0)] # 서 남 동 북
curSightIndex=sightDirection[sight]
checkCanGo=[0,0,0,0] #왼쪽부터 반시게방향으로 갈수있는 길인지 체크한 여부.

# 맵 초기화.
for i in range(row):
    gameMap.append(list(map(int,input().split())))

print(gameMap)
# 왼쪽 바라 보기 (방향 설정)
# 왼쪽이 0인지 확인
# 0이면 전진
# 이전에 있던 칸을 1로 채우기
haveGo=True
checkCount=0    # checkCount==4 일 때 haveGo 를 False로 한다.

while(haveGo): # 언제까지 반복해야하지?
    for i in range(len(checkCanGo)):
        if(not checkLeftSide(direction[curSightIndex],curPosition)):  #왼쪽확인 false: 갈수 없음 true: 갈수 있음.
            checkCanGo[curSightIndex]=1
            if(nextSight(curSightIndex)):
                curSightIndex=0
            else:
                curSightIndex+=1

            print(curSightIndex)
            checkCount+=1
            if(checkCount==4):
                haveGo=False
            print("갈수 없어요~")
        else:
            print(curPosition)
            checkCount=0
            print(prevPosition.posX,prevPosition.posY)
            gameMap[prevPosition.posX][prevPosition.posY]=1
            checkCanGoInit(checkCanGo)
            print(gameMap)
            print("갈 수 있어요~!~@ㅎㅎ")
            break

print(curPosition)
    ## 테스트 목적: checkLeftSide가 정상적으로 작동하는지를 확인해본다.
