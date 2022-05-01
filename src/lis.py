a = [10,11,2,4,45,41,55,6,91]
print a
b = {}

def form_result(key, result_dict, result, result_set):
	print key
	if not result_dict[key]:
		result_set.append(result)
		result = []
		#return result_set
	result.append(key)
	for v in result_dict[key]:
		form_result(v, result_dict, result, result_set)
	print result_set

def lis(b,a):
	if len(a) ==1:
		return []

	start_value = a[0]
	for i in a:
		if i>start_value:
			curr_value = i
			break
	end_points = []
	for i in a:
		#print i,start_value,curr_value
		if i > start_value and i <= curr_value:
			end_points.append(i)
			curr_value = i
	print 'end_points'
	print end_points
	return end_points

for i in range(len(a)):
	reverse_index = len(a) - 1 - i
	end_points = lis(b,a[reverse_index:])
	#print end_points
	b[a[reverse_index]] = end_points
	print b

print b
for key,value in b.iteritems():
	print 'key - ',key
	form_result(key, b, [], [])

"""

a = [10,11,2,4,45,41,55,6,91]

b = {}

def lis(b,a):
	curr_value = a[0]
	max_lis = []
	for i in a:
		if i > curr_value:
			max_lis.extend(b[i])
			break
	return max_lis

for i in range(len(a)):
	reverse_index = len(a) - 1 - i
	print reverse_index, a[reverse_index]
	if not b.get(a[reverse_index]):
		b[a[reverse_index]] = [a[reverse_index]]
	print b
	b[a[reverse_index]].extend(lis(b,a[reverse_index:]))
	print b
print b

"""
"""
a = [10,11,2,4,45,41,55,6,91]

b = {}

def lis(b,a):
	curr_value = a[0]
	max_lis = []
	for i in a:
		if i > curr_value:
			max_lis.append(b[i])
	return max(max_lis) if max_lis else 0

for i in range(len(a)):
	reverse_index = len(a) - 1 - i
	print reverse_index, a[reverse_index]
	if not b.get(a[reverse_index]):
		b[a[reverse_index]] = 1
	print b
	b[a[reverse_index]] += lis(b,a[reverse_index:])
	print b
print b
print max(b.values())
"""
