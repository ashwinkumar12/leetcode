a = [1,12, 11, 13, 5, 6]
print a
def rec_insertion_sort(a,n):
	print a,n
	if n<=1:
		print a,n, '-'
		return
	rec_insertion_sort(a,n-1)

	key = a[n-1]
	j = n-2
	print key,j,a
	while j>=0 and key < a[j]:
		a[j+1] = a[j]
		j -=1
	a[j+1] = key

rec_insertion_sort(a,len(a))
print a