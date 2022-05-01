a = [12, 11, 13, 5, 6]
print a
for i in range(1,len(a)):
	key = a[i]
	j = i-1
	while j>=0 and key < a[j]:
		print i,j,key,a[j],a
		a[j+1] = a[j]
		j -=1
		print a
	print a
	a[j+1] = key
	print a
print a			