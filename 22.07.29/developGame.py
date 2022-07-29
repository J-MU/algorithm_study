row,col=map(int,input().split())
posX,posY,sight=map(int,input().split())

map=list()

sightDirection=[0,3,2,1] #북 서 남 동
direction=[(-1,0),(0,-1),(1,0),(0,1)] # 서 남 동 북
curSightIndex=sightDirection[sight]

# 맵 초기화.
for i in range(row):
    map.append(list(map(int,input().split())))

# 왼쪽 바라 보기 (방향 설정)
# 왼쪽이 0인지 확인
# 0이면 전진
# 이전에 있던 칸을 1로 채우기

