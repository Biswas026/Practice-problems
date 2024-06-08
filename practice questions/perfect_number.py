def perfect(n):
    sum = 0
    for i in range(1,n):
        if n%i == 0:
            sum+=i

    if sum == n:
        print("Your given number is perfect")

    else:
        print("Your given number is not perfect")


perfect(6)
        
