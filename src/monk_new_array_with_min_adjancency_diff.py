"""
n,m = map(int,raw_input().split())
a = [0 for i in range(n)]

for i in range(n):
    a[i] = map(int, raw_input().split())
    
min_diff = []
for i in range(0,n-1):
    for val in a[i]:
        diff = []
        for j in range(m):
            row_diff_val = abs(val - a[i+1][j])
            diff.append(row_diff_val)
        min_diff.append(min(diff))
    if min(min_diff) == 0:
        break

print min(min_diff)
"""
def leastdiff(a1,a2):
    i,j = 0,0
    mindiff = abs(a1[0]-a2[0])
    while (i<m and j<m and mindiff!=0):
        diff = abs(a2[j]-a1[i])
        if(diff<mindiff):
            mindiff = diff
        if(a1[i]<a2[j]):
            i=i+1
        else:
            j = j+1
    return mindiff

n,m = map(int,raw_input().split())
a = []
for i in range(n):
    b = map(int,raw_input().split()) 
    b.sort()
    a.append(b)
mindiff = leastdiff(a[0],a[1])
for i in range(1,n-1):
    diff = leastdiff(a[i],a[i+1])
    if(diff<mindiff):
        mindiff=diff
    if(mindiff==0):
        break
print mindiff