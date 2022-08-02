# 백준 2583번 문제(그래프 탐색문제)
# https://www.acmicpc.net/problem/2583
from collections import deque



def bfs(x,y):
    count=0
    queue=deque()
    queue.append((x,y))
    area[y][x]=1
    while queue:
        count+=1
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if(nx<0 or ny<0 or nx>=col or ny>=row):
                continue
            if(area[ny][nx]==1):
                continue
            area[ny][nx]=1
            queue.append((nx,ny))
    return count
dx=[-1,0,1,0]
dy=[0,1,0,-1]

row,col,rectangleNum=map(int,input().split())
# print()
# print(row,col,rectangleNum)


area=[]

for i in range(row):
    area.append([0 for i in range(col)])


for i in range(rectangleNum):
    x1,y1,x2,y2=map(int,input().split())
    # print(x1,y1,x2,y2)
    for i in range(x2-x1):
        for j in range(y2-y1):
            area[j+y1][i+x1]=1

# for i in range(row-1,-1,-1):
#     print(area[i])

# print()
# print()
# print()
# print("result")
result=[]

for y in range(len(area)):
    for x in range(len(area[y])):
        if(area[y][x]==0):
            result.append(bfs(x,y))

result.sort()
print(len(result))
for i in result:
    print(i,end=" ")


