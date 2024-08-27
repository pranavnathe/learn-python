## ex: 2**4 = 16

def factorial(base, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * factorial(base, exp - 1)

## Driver Code  
num = 2
x = 4 
print(factorial(num, x))