a=int(input("Enter your first number"))
b=int(input("Enter your second number"))
i=1
j=1
c=[]
d=[]
while i<a:
    if a%i==0:
        c.append(i)
    i=i+1
while j<b:
    if b%j==0:
        d.append(j)
    j=j+1

if sum(c)==b and sum(d)==a:
    print("It is a amicable pair")
else:
    print("It is not an amicable pair")