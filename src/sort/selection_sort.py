a = [5, 1, 4, 2, 8]
#a = range(5)
for i in range(len(a)):
	for j in range(i+1,len(a)):
		print i,j,a[i],a[j], a
		if a[i] > a[j]:
			temp = a[i]
			a[i] = a[j]
			a[j] = temp

print a