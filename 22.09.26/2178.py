import sys

N,M=list(map(int,input().split()))

# print(N,M)

direction=[(1,0),(0,1),(-1,0),(0,-1)]

def bfs(curX,curY):
    count=0
    minCount=sys.maxsize
    # print(minCount)

    queue=list()
    # print(curX,curY)
    queue.append((curX,curY,count+1))
    graph[curY][curX]=0

    while(len(queue)):
        currentX,currentY,currentCount=queue.pop(0)
        if(currentX<1 or currentX>=M or currentY<1 or currentY>=N):
            continue
        if(currentX==M-1 and currentY==N-1):
            if(minCount>currentCount):
                minCount=currentCount
        for i in range(len(direction)):
            dX=currentX+direction[i][0]
            dY=currentY+direction[i][1]
            if(graph[dY][dX]==0):
                continue
            queue.append((dX,dY,currentCount+1))
            graph[currentY][currentX] = 0

    print(minCount)



graph=list()

for i in range(N):
    row=list(map(int,input()))
    graph.append(row)

for i in range(N):
    print(graph[i])

bfs(0,0)