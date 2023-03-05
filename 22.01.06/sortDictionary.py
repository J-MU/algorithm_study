# https://www.acmicpc.net/problem/1181
# 백준 1181 : 단어 정렬

N=int(input())

list_array=set()

for i in range(N):
    list_array.add(input())

array=list(list_array)
array.sort()
array.sort(key=lambda x:len(x))
for str in array:
    print(str)

