def frequency(string):
    p={}
    for i in string:
        count=1
        if i not in p.keys():
            p[i]=count
        else:
            p[i]=p[i]+1

    print(p)
frequency("we are what we are")
