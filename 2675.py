from collections import deque

str_num=int(input())

for i in range(str_num):
    repeat, str=input().split()
    repeat=int(repeat)

    str=deque(str)
    while len(str)>0:
        repeat_word=str.popleft()
        for i in range(repeat):
            print(repeat_word,end='')
    print()

