from collections import deque


dir=[(-1,0),(1,0),(0,1),(0,-1)]

def bfs(row,col):
    queue=deque()
    queue.append((row,col))
    graph[row][col]=0
    count=1

    while queue:
        row,col=queue.popleft()
        for dr,dc in dir:
            newRow=row+dr
            newCol=col+dc
            if newRow<0 or newRow>=N or newCol<0 or newCol>=N:
                continue
            if graph[newRow][newCol]==1:
                queue.append((newRow,newCol))
                count+=1
                graph[newRow][newCol]=0

    return count

def search():
    n=0
    m=0
    count=0
    for i in range(N):
        for j in range(N):
            if graph[i][j]==1:
                stack.append(bfs(i,j))
                count+=1

    return count

N=int(input())

graph=[]
stack=[]

for i in range(N):
    graph.append(list(map(int,input())))

print(search())
stack.sort()
for i in stack:
    print(i)
