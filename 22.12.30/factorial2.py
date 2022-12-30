def factorial(n):
    score=1
    for i in range(2,n+1):
        score*=i
    return score

print(factorial(10))