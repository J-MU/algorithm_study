stack=[]

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 5 2 3 1 으로 출력될것이라 예상
print(stack[::-1]) # 1 3 2 5
print(stack[0])
print(stack[-1])


