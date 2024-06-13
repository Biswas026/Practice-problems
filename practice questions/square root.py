# def square_root(n):
#     if x==0 or x==1:
#         return x
#
#     i = 1
#     result = 1
#
#     while(result <= x):
#         i+=1
#         result =i * i
#     return i-1



#binary search approach

def square_root(x):
    if x==0 or x==1:
        return x

    start = 1
    end = x//2

    while(start <= end):
        mid = (start + end)//2

        if mid*mid ==x:
            return mid

        if mid*mid < x:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
    return ans




x=100
print(square_root(x))