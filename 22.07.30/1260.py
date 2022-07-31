# 백준 1260번 문제(그래프 탐색문제)
# https://www.acmicpc.net/problem/1260
from collections import deque

def dfs(graph,v,visited):
    visited[v]=True
    print(v,end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph,start,visited):
   queue=deque([start])

   visited[start]=True

   while queue:
       v=queue.popleft()
       print(v,end=" ")

       for i in graph[v]:
           if not visited[i]:
               queue.append(i)
               visited[i]=True

vertexNum,edgeNum,startVertex=map(int,input().split())
visitedDFS=[False]*(vertexNum+1)
visitedBFS=[False]*(vertexNum+1)

graph=[]
for i in range(vertexNum+1):
    graph.append([])

for i in range(edgeNum):
    startPoint,endPoint=map(int,input().split())
    graph[startPoint].append(endPoint)
    graph[endPoint].append(startPoint)
# 정렬을 해줘야 할 지도?
for list in graph:
    list.sort()

dfs(graph,startVertex,visitedDFS)
print()
bfs(graph,startVertex,visitedBFS)


