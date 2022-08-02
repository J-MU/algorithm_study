# 이것이 코딩테스트다 -나동빈저자 (Chapter5 DFS,BFS)
# p.149 음료수 얼려 먹기
# 출처: ??
# 07.31


from collections import deque

def bfs(graph,startRow,startCol,visited):
    queue=deque([(startRow,startCol)])
    visited[startRow][startCol]=True

    while queue:
        v=queue.popleft()
        print(v,end=" ")
        for position in graph[v[0]][v[1]]:
            if not visited[position[0]][position[1]]:
                queue.append(position)
                visited[position[0]][position[1]]=True

def linkStuckIndex(row,col,graph,maxRow,maxCol):
    if(row+1<maxRow and array[row+1][col]==0):
        graph[row][col].append((row+1,col))
        graph[row+1][col].append((row,col))
    if(col+1<maxCol and array[row][col+1]==0):
        graph[row][col].append((row, col+1))
        graph[row][col+1].append((row, col))

def hasFalseInVisited(visited):
    for i in range(len(visited)):
        for j in range(len(visited[i])):
            if not visited[i][j]:
                return [i,j]

    return -1

N,M=map(int,input().split())
visited=[False]*N*M

count=0
array=list()
for i in range(N):
    array.append(list(map(int,list(input()))))

graph = [[[] for _ in range(M)] for _ in range(N)]

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if array[i][j]==0:
            linkStuckIndex(i,j,graph,N,M)


visited = [[0 for _ in range(M)] for _ in range(N)]
for i in range(len(visited)):
    for j in range(len(visited[i])):
        if(array[i][j]==1):
            visited[i][j]=True


print("------------graph--------------")
for i in range(len(graph)):
    print(graph[i])
print()

print("-----------array---------------")
print(array)

print("------------visited--------------")
for i in range(len(visited)):
    print(visited[i])
print()

while True:
    falseIndex=hasFalseInVisited(visited)
    if(falseIndex==-1):
        break
    count+=1
    bfs(graph,falseIndex[0],falseIndex[1],visited)
    print()
    print()

print(count)


count = 0


# 테스트 케이스
# 4 5
# 00110
# 00011
# 11111
# 00000
#
# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111
