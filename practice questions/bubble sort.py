def b_sort(list1):
    for j in range(len(list1)-1):
        for i in range(len(list1)-1-j):
            if list1[i]> list1[i+1]:
                list1[i],list1[i+1] = list1[i+1],list1[i]

    print(list1)


b_sort([10,100,32,12,10,55])