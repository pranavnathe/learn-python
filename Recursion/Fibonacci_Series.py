## Fibonacci Series

def fib(num):
    if num <= 1:
        return num
    else:
        return fib(num - 1) + fib(num - 2)

## Driver Code
num = 8
# print(fib(num))
for n in range(num):
    print(fib(n))