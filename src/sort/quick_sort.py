def quick_sort(arr, low, high):
	if low < high:
		p = partition(arr, low, high)
		print 'p---', p
		quick_sort(arr, low, p-1)
		quick_sort(arr, p+1, high)

def partition(arr, low, high):
	print arr, low, high
	p = arr[high]
	print 'p - ',p
	j = low
	print 'j - ',j
	for i in range(low,high):
		print 'i,j - ',i,j
		print 'arr.i - arr.j :',arr[i],arr[j]
		if arr[i]<=p:
			print 'swap'
			temp = arr[i]
			arr[i] = arr[j]
			arr[j] = temp
			j += 1
			print 'after swap : ',arr
	print j,p
	temp = arr[high]
	arr[high] = arr[j]
	arr[j] = temp
	print arr
	print j
	#return
	return j

arr=[4,5,2,1,3]
quick_sort(arr,0,len(arr)-1)
print arr