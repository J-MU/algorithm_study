#백준 12605 단어 뒤집기 문제
# https://www.acmicpc.net/problem/12605

# N -> 케이스의 개수이다.
# 문장이 주어지면 이를 스페이스를 기준으로 split하여 stack에 삽입한다.

N=int(input())
sentence= arr = [[0 for j in range(N)] for i in range(25)]


for i in range(N):
    sentence[i]=input().split()

for i in range(N) :
    nth_sentence=sentence[i]
    len_sentece=len(nth_sentence);
    print("Case #%d: " %(i+1),end='');

    for word_length in range(len_sentece):
        #print("nth_sentence:",nth_sentence)
        if(word_length==len_sentece-1):
            print(nth_sentence.pop(),end='')
        else:
            print(nth_sentence.pop(), end=' ')
    print()
