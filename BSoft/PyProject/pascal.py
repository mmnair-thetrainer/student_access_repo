from math import factorial
n = 5
for i in range(n):
    first = n-i+1
    second = i+1
    for j in range(first):
        print(end=" ")
    for j in range(second):
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    print()