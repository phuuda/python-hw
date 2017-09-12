def fibonacci(n):

    if isinstance(n, int) and n >= 0:

        if n == 1 or n == 0:
            return n

        if n == 2:
            return 1

        if n > 2:
    
            n1, n2 = 1, 1
            n3 = n1 + n2
            
            for i in range(n-3):
            
                n1 = n2
                n2 = n3
                n3 = n1 + n2

            return n3

    else:
        return "please enter positive integer"
        
print(fibonacci(20.4))
print(fibonacci('door'))
print(fibonacci(-5))
print(fibonacci(20))
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
