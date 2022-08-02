# 이것이 코딩테스트다 -나동빈저자 (Chapter5 DFS,BFS)
# p.149 음료수 얼려 먹기
# 출처: ??
# 07.31

# N,M 을 공백으로 구분하여 입력받기
n,m=map(int,input().split())

# 2차원 리스트의 맵 정보 입력받기
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    # 주어진 버위를 벗아나는 경우에는 즉시 종료
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1

print(result)

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