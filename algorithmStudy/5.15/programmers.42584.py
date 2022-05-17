# https://programmers.co.kr/learn/courses/30/lessons/42584
# programmers 코테연습kit 스택/큐 - 주식가격 문제

prices=[1,2,3,2,3]
down_time=[]

for start in range(len(prices)):
    if start==len(prices)-1:
        down_time.append(0)

    for end in range(start+1,len(prices)):
        if prices[start]>prices[end]:
            down_time.append(end-start)
            break
        elif end==len(prices)-1:
            down_time.append(end - start)

print(down_time) #for문 밖에 있어야함