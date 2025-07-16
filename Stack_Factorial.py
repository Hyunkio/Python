def stack_factorial(n):
    stack = []
    result = 1
    
    while n > 0: #5 - 4 - 3 - 2 - 1
        stack.append(n)
        n -= 1
        
    while stack:
        result *= stack.pop()
        
    return result

print(stack_factorial(5))