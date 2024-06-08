
a=2130021
reverse_num = 0
while a>0:
    n = a%10
    a = a//10
    reverse_num = reverse_num*10 + n
print(reverse_num)
