# https://programmers.co.kr/learn/courses/30/lessons/42583
# 프로그래머스 코테연습kit 스택/큐 다리를 지나는 트럭 문제
from collections import deque

bridge_length=100
weight=100
truck_weight=[10,10,10,10,10,10,10,10,10,10]
truck_weight_deque=deque(truck_weight)

bridge=deque()
on_bridge_weight=0

# Idea : 1초에 두가지 작업을 진행한다.
# 1. bride위에 있는 트럭중 다 건넌 트럭이 있는지 확인한다.
# 2. 다 건넌 트럭이 있으면 pop한다.
# 3. bride<2이하인지 확인한다.
# 4. bride가 full상태가 아니고 && 다음 순서의 트럭이 올라섰을때 wieght를 초과하지 않는다면 트럭을 append한다.
time=0

while len(truck_weight_deque)>0 or len(bridge)>0:
    if(len(truck_weight_deque)==0):
        if len(bridge) > 0 and bridge[0][1] == bridge_length:
            exit_truck = bridge.popleft()
            on_bridge_weight -= exit_truck[0]

        for i in range(len(bridge)):
            bridge[i][1] += 1

        time += 1

        continue
    if len(bridge)>0 and bridge[0][1]==bridge_length:
        exit_truck=bridge.popleft()
        on_bridge_weight-=exit_truck[0]

    if len(bridge)<bridge_length and (on_bridge_weight+truck_weight_deque[0])<=weight:
        bridge.append([truck_weight_deque[0],0])
        enter_weight=truck_weight_deque.popleft()
        on_bridge_weight+=enter_weight

    for i in range(len(bridge)):
        bridge[i][1]+=1

    time+=1
    print(bridge)

print(time)




