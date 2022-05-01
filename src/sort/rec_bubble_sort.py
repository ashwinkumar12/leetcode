a = [5, 1, 4, 2, 8]

def rec_bubble_sort(a, n):
	#print a, n
	if n == 1:
		return a
	else:
		for i in range(n):
			if i+1<n and a[i] > a[i+1]:
				temp = a[i+1]
				a[i+1] = a[i]
				a[i] = temp
		#print a
		rec_bubble_sort(a, n-1)

rec_bubble_sort(a, len(a))
print a
