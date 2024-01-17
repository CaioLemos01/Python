precision = 85
sumS = 0
sumC = 0
sumE = 0
x = 1.5
y = 1

def factorial(n):
    if(n == 0): return 1
    elif(n == 1): return 1
    else:
        factorial = n
        for j in range(1, n, 1):
            if(n - j == 0): return
            factorial *= (n - j)
    return factorial

# Função Seno
for n in range(0, precision, 1):
    partialSum = ((-1)**n)*((x**(2*n + 1))/factorial((2*n + 1)))
    sumS = sumS + partialSum

# Função Cosseno
for n in range(0, precision, 1):
    partialSumC = ((-1)**n)*((x**(2*n))/factorial((2*n)))
    sumC = sumC + partialSumC

# Função e^x
for n in range(0, precision, 1):
    partialSumE = ((y**(n))/factorial((n)))
    sumE = sumE + partialSumE

# print(f'{sum:.10f}')
print(f'Function sin(x): {sumS}')
print(f'Function cos(x): {sumC}')
print(f'Function e^x: {sumE}')