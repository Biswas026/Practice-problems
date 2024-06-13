def ins_sort(list1):
    for index in range(1, len(list1)):
        current_element = list1[index]
        pos = index

        while pos > 0 and current_element < list1[pos - 1]:
            list1[pos] = list1[pos - 1]
            pos -= 1

        list1[pos] = current_element



list1 = [100, 230, 20, 1, 5, 35, 400]
ins_sort(list1)
print(list1)
