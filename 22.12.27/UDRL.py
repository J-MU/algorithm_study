def move_left():
    global cur
    future_pos=[cur[0],cur[1]-1]
    if(check_out(future_pos)):
        cur=future_pos


def move_right():
    global cur
    future_pos=[cur[0],cur[1]+1]
    if(check_out(future_pos)):
        cur=future_pos
        print(cur)

def move_up():
    global cur
    future_pos=[cur[0]-1,cur[1]]
    if(check_out(future_pos)):
        cur=future_pos

def move_down():
    global cur
    future_pos=[cur[0]+1,cur[1]]
    if(check_out(future_pos)):
        cur=future_pos

def check_out(future_pos):
    if(future_pos[0]>0 and future_pos[0]<=N and future_pos[1]>0 and future_pos[1] <=N):
        return 1
    else:
        return 0

def move(dir):
    print(cur)
    if(dir=='L'):
        print(dir)
        move_left()
    elif(dir=='R'):
        print(dir)
        move_right()
    elif(dir=='U'):
        print(dir)
        move_up()
    elif(dir=='D'):
        print(dir)
        move_down()
    else:
        print("Shit")

N=int(input())

arr=[]
arr=input().split()

cur=[1,1]

MAX_ROW=N
MAX_COL=N

for dir in arr:
    move(dir)

print(cur)