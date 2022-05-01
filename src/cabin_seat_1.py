import itertools

from pprint import pprint
l_l = [[2,4], [4,3], [1,1]]

ll = {}

def type_0(i,j):
    l = []
    if i==1:
        for k in range(i*j):
            if k%i == 0:
                l.append((n,k,'w'))
        return l
    for k in range(i*j):
        if k%i == 0:
            l.append((0,k,'w'))
        elif k%i == i-1:
            l.append((0,k,'i'))
        else:
            l.append((0,k,'c'))
    return l

def type_n(n,i,j):
    l = []
    if i==1:
        for k in range(i*j):
            if k%i == 0:
                l.append((n,k,'w'))
        return l
        
    for k in range(i*j):
        if k%i == 0:
            l.append((n,k,'i'))
        elif k%i == i-1:
            l.append((n,k,'w'))
        else:
            l.append((n,k,'c'))
    return l

def type_c(n,i,j):
    l = []
    for k in range(i*j):
        if k%i == 0 or k%i==i-1:
            l.append((n,k,'i'))
        else:
            l.append((n,k,'c'))
    return l

len_l_l = len(l_l)
ll[0] = type_0(l_l[0][0],l_l[0][1])    
for i,j in enumerate(l_l[1:-1]):
    ll[i+1] = type_c(i+1,j[0],j[1])
ll[len_l_l-1] = type_n(len_l_l-1,l_l[-1][0],l_l[-1][1])

#print ll

def print_dict(data):
    for i,j in data.iteritems():
        print i,j
        print '\n'

print_dict(ll)

b = {}
for i,j in ll.iteritems():
    split = l_l[i][0]
    b[i] = [j[k:k+split] for k in range(0,len(j),split)]
 
print_dict(b)   

d = b.values()
print d

c = itertools.izip_longest(*d)
print c

print "\n"

p = []
for i in c:
    print i
    p.extend(list(i))
print "\n"

print p
for i in p:
    print i
    
result = []
[result.extend(el) for el in p if el]
print result
for i in result:
    print i

order = {'i':0,'w':1,'c':2}
result = sorted(result,key=lambda x:order[x[2]])
print '\n'
print result
for i in result:
    print i
#pprint(result)
