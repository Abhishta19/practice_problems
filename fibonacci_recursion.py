def fibonacci(num):
    if num<=0:
        return 0
    elif num==1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)

num_terms=10
for i in range(num_terms):
    print(fibonacci(i), end=" ")

def fibonacci_iterative(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, num + 1):  # <-- use range, not tuple
        a, b = b, a + b
    return b


num = 10
for i in range(num):
    print(fibonacci_iterative(i), end=" ")
