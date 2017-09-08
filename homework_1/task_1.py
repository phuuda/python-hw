def fibonacci(n):
    
    n1, n2 = 1, 1
    n3 = n1 + n2
    
    for i in range(n-3):
    
        n1 = n2
        n2 = n3
        n3 = n1 + n2

    return n3

print(fibonacci(20))
