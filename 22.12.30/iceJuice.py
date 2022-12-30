from collections import deque
dir=[(-1,0),(0,-1),(1,0),(0,1)]

def bfs(juice_box,row,col):
    queue=deque()
    queue.append((row,col))
    while queue:
        row, col = queue.popleft()
        for (dr,dc) in dir:
            newRow=row+dr
            newCol=col+dc

            if(newRow<0 or newRow>=N or newCol<0 or newCol>=M):
                continue
            elif(juice_box[newRow][newCol]==0):
                queue.append((newRow,newCol))
                juice_box[newRow][newCol]=1
            else:
                continue

def search(juice_box):
    global count
    for i in range(N):
        for j in range(M):
            if(juice_box[i][j]==0):
                bfs(juice_box,i,j)
                count+=1

count=0
juice_box=[]

N,M=map(int,input().split())

for i in range(N):
    juice_box.append(list(map(int,input())))

search(juice_box)
print(count)
