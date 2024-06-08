def sum(string):
    sum = 0
    for i in string:
        if i.isdigit():
            sum +=int(i)

    print(sum)

sum("B2is4w66as123")
