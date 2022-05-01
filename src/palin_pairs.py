'''
# Sample code to perform I/O:

name = raw_input()          # Reading input from STDIN
print 'Hi, %s.' % name      # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
from collections import Counter

# Write your code here
n = int(raw_input())
a = list()
for i in range(n):
    a.append(raw_input())
b = list()
for i in a:
    b.append(i[::-1])

def count_items(arr,item):
    #print arr,item
    count_dict = Counter(arr)
    return count_dict[item]
    
def num_palin_pairs_v1(a,b):
    count = 0
    for i in range(len(a)):
        count += count_items(b[i+1:],a[i])
    return count

def num_palin_pairs(arr):
    l = len(arr)
    if l == 1:
        return 0
    count = 0
    
    for i in range(l):
        for j in range(i+1,l):
            if a[i][::-1] == a[j]:
                count+=1
    return count            

print num_palin_pairs_v1(a,b)