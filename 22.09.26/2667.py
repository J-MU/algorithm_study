N=int(input())

print(N)

direction=[[1,0],[0,-1],[-1,0],[0,1]]
queue=list()
count_list=[]
max_count=0

def bfs(curX,curY,count):
    global max_count
    count=1
    max_count=1

    print((curX,curY,count),end=' ')
    graph[curX][curY]=0
    queue.append((curX,curY,count))
    while(len(queue)>0):
        if max_count < count:
            max_count = count
        for i in range(len(direction)):
            if(graph[curX+direction[i]][curY+direction[i]]==1):
                queue.append((curX,curY,count+1))
            if i==3:
                curX,curY,count=queue.pop(0)






graph=[[0]*(N+2) for _ in range(N+2)]

for i in range(N):
    row=list(map(int,input()))
    for j in range(N):
        graph[i+1][j+1]=row[j]

for i in range(N+2):
    print(graph[i])

curX,curY=[1,1]

print(curX,curY)

for i in range(N):
    for j in range(N):
        if(graph[i][j]==1):
            # 여기서 그래프 탐색 시작해야함.
