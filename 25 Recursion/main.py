# factorial(7) = 7*6*5*4*3*2*1

def factorial(num):

    if(num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1))

num = 7
print("Number:", num)
print("Factorial:", factorial(num))


def fibonacci(n):
    if (n==0):
        return n
    elif (n == 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
    
print(fibonacci(6))