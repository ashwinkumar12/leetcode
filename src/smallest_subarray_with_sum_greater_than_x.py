input = [1,10,3,40,18]
x = 50
length = len(input)

global min_length
min_length = 3

curr_sum = 0 

start = 0
end = 0

def find_sum(input, start, end, min_length):
	print input, start, end, min_length, x, len(input)
	curr_sum = 0
	if start <= len(input):
		print 'inside first if'
		if start == end:
			find_sum(input, start, end+1, min_length)
		else:
			for i in range(start, end):
				if input[i] > x:
					return 1
				curr_sum += input[i]
				print i, curr_sum
				if curr_sum > x:
					print 'greater than'
					if (end - start + 1) < min_length:
						min_length = end - start
					print curr_sum, start +1, end, min_length, i
					find_sum(input, start + 1, end, min_length)
				elif end < len(input)-1:
					print 'inside elseif'
					print curr_sum, start, end+1, min_length, i
					find_sum(input, start, end+1, min_length)
	else:
		print 'inside else'
		return min_length

print 'min_length - ',find_sum(input, 0, 0, min_length)
