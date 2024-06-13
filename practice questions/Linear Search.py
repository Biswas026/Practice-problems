def search(List1,key):
    for i in range(len(List1)):
        if key == List1[i]:
            print("Key element is found")
            break
    else:
         print("Key element is not found")


List1 = [1,2,3,4,5]
search(List1,2)
