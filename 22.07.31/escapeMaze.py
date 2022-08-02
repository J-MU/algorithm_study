# 이것이 코딩테스트다 -나동빈저자 (Chapter5 DFS,BFS)
# p.149 음료수 얼려 먹기
# 출처: ??
# 08.01
from collections import deque


def bfs(x,y):
    queue=deque()
    queue.append((x,y))

    while queue:
        x,y=queue.popleft()

        for i in range(len(dx)): #동남서북 4가지 방향.
            nx=dx[i]+x
            ny=dy[i]+y

            if nx<0 or nx>=col or ny<0 or ny>=row:
                continue

            if graph[ny][nx]==0:
                continue

            if graph[ny][nx]==1:
                graph[ny][nx]=graph[y][x]+1
                queue.append((nx,ny))

    return graph[row-1][col-1]



dx=[-1,0,1,0]
dy=[0,1,0,-1]

# row col input받아오기.
row,col=map(int,input().split())


# graph 초기화.
graph=[]
for i in range(row):
    graph.append(list(map(int,input())))

for i in range(len(graph)):
    print(graph[i])

result=bfs(0,0)
print(result)
