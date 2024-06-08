#iterative approach

def average(List):
    sum=0
    for i in List:
        sum += i

    print(sum/len(List))


average([1,2,3,4,5])


#recursive approach

def average2(List):
    if len(List)==1:
        return List[0]
    else:
        return List[0] +  average2(List[1:])
    

List = [1,2,3,4,50]
sum = average2(List)
print(sum/len(List))
