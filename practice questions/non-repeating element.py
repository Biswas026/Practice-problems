
def firstNonRepeating(arr, n):

	
	for i in range(n):
		j = 0
		# Checking if ith element is present in array
		while(j < n):
			if (i != j and arr[i] == arr[j]):
				break
			j += 1
		
		if (j == n):
			return arr[i]

	return -1


arr = [9, 4, 9, 6, 7, 4]
n = len(arr)
print(firstNonRepeating(arr, n))


