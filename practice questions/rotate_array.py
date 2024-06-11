def rotate(A,D,N):
    new_A=[]
    for i in range(N):
        new_A.append(0)
        
    for i in range(N):
        if i-D<0:
            new_A[N+(i-D)] = A[i]
        else:
            new_A[i-D] = A[i]
    return new_A


arr = [1, 2, 3, 4, 5, 6, 7,8,9,10]
d = 2
N = len(arr)
print("Our original array",arr)

arr = rotate(arr, d, N)
print("Rotated array",arr)
