#iterative approach
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i

    print("Factorial of the number",fact)

factorial(5)

#recursive approach
def factorial2(n):
    if n==1:
        return 1
    else:
        return n * factorial2(n-1)

factori = factorial2(5)
print("Factorial of the number",factori)
