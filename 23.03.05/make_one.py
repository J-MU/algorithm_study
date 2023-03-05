
def operandA(i,n):
    if(i+1 >n):
        return False

    if (d[i+1] ==0 or d[i + 1] > d[i] + 1):
        d[i + 1] = d[i] + 1
    return True


def operandB(i,n):
    if(i*2 >n):
        return False

    if (d[i*2] ==0 or d[i * 2] > d[i] + 1):
        d[i * 2] = d[i] + 1
    return True

def operandC(i,n):
    if(i*3 >n):
        return False

    if (d[i*3] ==0 or d[i * 3] > d[i] + 1):
        d[i * 3] = d[i] + 1
    return True

def operandD(i,n):
    if(i*5 >n):
        return False

    if (d[i*5] ==0 or d[i * 5] > d[i] + 1):
        d[i * 5] = d[i] + 1
    return True

x=int(input())

d=[0]*(x+1)
d[1]=0


for i in range(1,x+1):
    if (not operandA(i,x)) :
        continue

    if (not operandB(i, x)):
        continue

    if (not operandC(i, x)):
        continue

    if (not operandD(i, x)):
        continue

print(d[26])