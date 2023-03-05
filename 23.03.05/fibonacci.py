import time


def fibo(x):
    if x==1 or x==2:
        return 1

    print(x)
    return fibo(x-1)+fibo(x-2);


start=time.time()
print(fibo(40))
end=time.time()

print(f"{end-start:.5f} sec")