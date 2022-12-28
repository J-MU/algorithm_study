def search():
    global curX,curY,dir
    newX=curX+dx[dir]
    newY=curY+dy[dir]
    if(map_array[newY][newX]==0):
        move(newX,newY)
        return 1
    else:
        spin()
        return 0

def move(newX,newY):
    global curX,curY,move_count
    map_array[curY][curX]=1
    curX=newX
    curY=newY
    move_count=move_count+1

def spin():
    global dir
    dir=(dir+1)%4

move_count=0
dx=[0,-1,0,1]
dy=[-1,0,1,0]

ROW,COL=map(int,input().split())

curX,curY,dir=map(int,input().split())

map_array=[]
for row in range(ROW):
    map_array.append(list(map(int,input().split())))

while 1:
    for i in range(4):
        is_find=search()
        if(is_find):
            break
    if(is_find==0):
        move(curX-dx[dir],curY-dy[dir])




