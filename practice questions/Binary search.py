def search(List1,key):
    List1.sort()
    left = 0
    right = len(List1) - 1
    found = False

    while left<=right and not found:
        mid = (left + right)//2
        if List1[mid] == key:
            found = True
        elif key>List1[mid]:
            left = mid + 1
        else:
            right = mid - 1

    if found:
        print("key found")
    else:
        print("Key not found")

List1 = [1,2,3,4,5]
search(List1,4)

