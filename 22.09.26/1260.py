
def dfs(start_vertex):
    print(start_vertex, end=' ')
    visited[start_vertex] = 1

    for i in range(len(graph[start_vertex])):
        if visited[graph[start_vertex][i]]==1:
            continue
        else:
            dfs(graph[start_vertex][i])

def bfs(start_vertex):
    queue=list()
    queue.append(start_vertex)
    visited[start_vertex]=1
    while(len(queue)):
        vertex=queue.pop(0)
        print(vertex,end=" ")
        for i in range(len(graph[vertex])):
            if(visited[graph[vertex][i]]==1):
                continue
            queue.append(graph[vertex][i])
            visited[graph[vertex][i]]=1

visited=[]

vertex,edge,init_vertex=list(map(int,input().split()))
# print(vertex,edge,init_vertex)

# 이차원 배열 생성.
graph=list()
for i in range(vertex+1):
    graph.append(list())
    visited.append(0)


for i in range(edge):
    first_vertex,second_vertex=list(map(int,input().split()))
    graph[first_vertex].append(second_vertex)
    graph[second_vertex].append(first_vertex)

for i in range(vertex+1):
    graph[i].sort()

dfs(init_vertex)
print()
for i in range(len(visited)):
    visited[i]=0

bfs(init_vertex)



