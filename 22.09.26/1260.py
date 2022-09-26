
def dfs(start_vertex):
    print(start_vertex, end=' ')
    visited[start_vertex] = 1

    for i in range(len(graph[start_vertex])):
        if visited[graph[start_vertex][i]]==1:
            continue
        else:
            dfs(graph[start_vertex][i])

visited=[]

vertex,edge,init_vertex=list(map(int,input().split()))
print(vertex,edge,init_vertex)

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
    print(graph[i])

dfs(init_vertex)



