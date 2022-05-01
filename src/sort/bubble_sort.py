a = [5, 1, 4, 2, 8]
a = range(5)
for j in range(len(a)):
	count = 0
	for i in range(len(a)):
		if i+1<len(a):
			print a[i], a[i+1]
			if a[i] > a[i+1]:
				count += 1
				temp = a[i+1]
				a[i+1] = a[i]
				a[i] = temp
		print a
	if count == 0:
		print j
		break

print a