N,M=list(map(int,input().split()))

print(N,M)

def bfs(curX,curY):
    print(curX,curY)

    if(graph[curX+1][curY]==1):
        bfs(curX+1,curY)
    if(graph[curX][curY-1]==1):
        bfs(curX, curY-1)
    if(graph[curX-1][curY]==1):
        bfs(curX,curY+1)
    if(graph[curX][curY+1]==1):
        bfs(curX,curY+1)



graph=[[0]*(M+2) for _ in range(N+2)]

for i in range(N):
    row=list(map(int,input()))
    for j in range(M):
        graph[i+1][j+1]=row[j]

for i in range(N+2):
    print(graph[i])

curX,curY=[1,1]

print(curX,curY)

# bfs(curX,curY)