"""
#Frog jump brute force recursion
def frog_jump_steps(jump, index, step_size):
	for i in range(index+1, len(jump)):
		print jump, ' i - ', i, jump[i], ' index - ',index, jump[index]
		gap = jump[i] - jump[index]
		print gap
		if gap >= step_size-1 and gap <= step_size+1:
			if frog_jump_steps(jump, i, gap):
				return True
	return index == len(jump) - 1
"""
"""
def frog_jump_steps(jump, index, step_size):
	for i in range(index+1, len(jump)):
		print jump, ' i - ', i, jump[i], ' index - ',index, jump[index]
		gap = jump[i] - jump[index]
		print gap
		if gap >= step_size-1 and gap <= step_size+1:
			if frog_jump_steps(jump, i, gap):
				return True
		else:
			break
	return index == len(jump) - 1

print frog_jump_steps(jump, 0, 0)
"""
jump = [0,1,3,5,8,11,15]

def frog_jump_steps(jump):
	previous_gap = 0
	for i in range(len(jump)-1):
		next_gap = jump[i] - jump[i+1]
		print next_gap
		if next_gap not in range(previous_gap-1,previous_gap+2):
			return False
		previous_gap = next_gap
	return True

print frog_jump_steps(jump)