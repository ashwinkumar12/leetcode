def merge(left, right):
    if not len(left) or not len(right):
        return left or right
 
    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i+= 1
        else:
            result.append(right[j])
            j+= 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
 
    return result
 
def mergesort(list):
    if len(list) < 2:
        return list
 
    middle = len(list)/2
    left = mergesort(list[:middle])
    right = mergesort(list[middle:]) 
    return merge(left, right)
     
seq = [12, 11, 13, 5, 6, 7]
print("Given array is")
print(seq); 
print("\n")
print("Sorted array is")
print(mergesort(seq))

"""
def mergesort(arr, l, r):
	if l<r:
		m = (l+r)//2
		print arr, l, m, r

		mergesort(arr,l,m)
		print 'lmr1 - ',l,m,r 
		mergesort(arr,m+1,r)
		print 'lmr2 - ',l,m,r
		a = arr[l:m+1]
		a.append(90)
		print 'a - ',a
		b = arr[m+1:r+1]
		b.append(90)
		print 'b - ',b
		i = 0
		j = 0

		for k in range(l,r+1):
			print k
			if a[i] <= b[j]:
				arr[k] = a[i]
				i += 1
			else:
				arr[k] = b[j]
				j += 1
			k += 1
			print arr
		print arr


arr = [4,0,6,1,2]
mergesort(arr, 0, len(arr)-1)
print arr
"""