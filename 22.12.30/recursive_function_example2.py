def recursive_function(i):
    if(i==100):
        return
    print("재귀함수 호출",i)
    recursive_function(i+1)
    print(i,'번째 재귀함수를 종료합니다.')

recursive_function(1)