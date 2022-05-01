a = [[4,6],[7,9],[10,14]]
new = [1,2]
a.append(new)
print a
a = sorted(a,key = lambda x:x[0])
print a

temp = list()
i = 1
temp.append(a[0])
while i<len(a):
	b = a[i]
	c = temp[-1]
	print b,c
	if c[1]>=b[0]:
		temp.pop()
		temp.append([min(b[0],c[0]), max(b[1],c[1])])
	else:
		temp.append(b)
	i+=1
	print "temp - ",temp
print temp