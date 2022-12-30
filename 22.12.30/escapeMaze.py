from collections import deque


def bfs(graph,row,col):
    graph[row][col]=1
    queue=deque()
    queue.append((row,col))

    while queue:
        row,col=queue.popleft()
        for dr,dc in dir:
            newRow=row+dr
            newCol=col+dc
            if(newRow<0 or newRow>=N or newCol<0 or newCol>=M):
                continue
            elif(graph[newRow][newCol]==0 or graph[newRow][newCol]>1):
                continue
            else:
                queue.append((newRow,newCol))
                graph[newRow][newCol]=graph[row][col]+1

dir=[(-1,0),(1,0),(0,-1),(0,1)]

N,M=map(int,input().split())
graph=[]
for i in range(N):
    graph.append(list(map(int,input())))


bfs(graph,0,0)
print(graph[N-1][M-1])