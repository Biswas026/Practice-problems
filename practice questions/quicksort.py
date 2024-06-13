def pivot_place(list1,first,last):
    pivot = list1[first]
    left = first + 1
    right = last
    while True:
        while left<=right and list1[left] <= pivot:
            left = left + 1

        while left<=right and list1[right] >= pivot:
            right = right - 1

        if left > right:
            break
        else:
            list1[left],list1[right] = list1[right],list1[left]

    list1[first],list1[right] = list1[right],list1[first]
    return right


def q_sort(list1, first, last):
    if first<last:
        p = pivot_place(list1,first,last)
        q_sort(list1,first,p-1)
        q_sort(list1,p+1,last)


list1=[100,230,20,1,5,35,400]
q_sort(list1,0,len(list1)-1)
print(list1)