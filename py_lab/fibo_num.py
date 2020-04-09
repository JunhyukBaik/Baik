#!/usr/bin/python3

def fibo(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

a = int(input("fibonacci number? "))
for i in range(1, a+1):
    print(fibo(i), end=' ')

print("")
print(fibo(a))
