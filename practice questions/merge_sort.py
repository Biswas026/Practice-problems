def mergesort(list1):
    if len(list1) > 1:
        mid = len(list1) // 2
        left_list = list1[:mid]
        right_list = list1[mid:]

        mergesort(left_list)
        mergesort(right_list)

        i = 0
        j = 0
        k = 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list1[k] = left_list[i]
                i += 1
            else:
                list1[k] = right_list[j]
                j += 1
            k += 1

        while i < len(left_list):
            list1[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            list1[k] = right_list[j]
            j += 1
            k += 1



list1 = [100, 230, 20, 1, 5, 35, 400]
mergesort(list1)
print(list1)
