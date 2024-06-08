#iterative approach
def armstrong(number):
    length = len(str(number))
    temp = 0
    for i in str(number):
        temp +=int(i)**length

    if temp == number:
        print("Your number is armstrong number")

    else:
        print("Your number is not armstrong number")


armstrong(153)


#recursive approach
def armstrong2(str_number,i):
    if i == len(str_number):
        return 0
    return int(str_number[i]) ** len(str_number) + armstrong2(str_number,i+1)

number = "153"

if number == str(armstrong2(number,0)):
    print("Your number is armstrong number")
else:
    print("Your number is not armstrong number")
    
