#This is my TCS question, the main catch over here is unlike other fibonacci series problem here we have to sum the series,if you want to print only then you have to make changes over here.

#recursive approach

##def fibonacci(n):
##    if n==0 or n==1:
##        return n
##    return fibonacci(n-1) + fibonacci(n-2)
##
##sum = 0
##term=eval(input("Give the nth term"))
##
##for i in range(term):
##          sum+=fibonacci(i)
##
##print(f" The sum till the {term}th term will be",sum)



#iterative approach

term = eval(input("Give the nth term"))
sum = 0
list = [0,1]
for i in range(term - 2):   
  list.append(list[-1]+list[-2])
  print(list)

for i in list:
    sum+=i
print(f" The sum till the {term}th term will be",sum)

         
        
