def cap_fl(string):
    a=string.split()
    new_string=""
    for i in a:
        sub_string = ""
        for x,j in enumerate(i):
           
            if j == i[0] or j == i[len(i)-1] and x==0 or x==len(i)-1:
                print(j)
                sub_string += j.upper()
            else:
                sub_string += j

        new_string+=sub_string + ' '


    print(new_string)

cap_fl("biswas is a good boy")
