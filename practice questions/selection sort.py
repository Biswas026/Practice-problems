def s_sort(list1):
    for i in range(len(list1)-1):
        m_ind = i
        for j in range(i+1,len(list1)):
            if list1[j]<list1[m_ind]:
                m_ind = j
        list1[i], list1[m_ind] = list1[m_ind], list1[i]

    print(list1)


s_sort([100,20,30,5,123,150,54])