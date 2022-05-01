from copy import copy
from pprint import pprint
class Solution(object):
    def __init__(self):
        self.k = set()

    def a(self,v,le):
        if le<len(v):
            v1 = copy(v)
            v[le] = -v[le]
            #print v
            #print v1
            self.k.add(self.a(v,le+1))
            self.k.add(self.a(v1,le+1))
        return tuple(v)

    def findTargetSumWays(self, nums, S):
        value = nums
        l=len(value)
        c=0
        for i in range(l):
            self.k.add(self.a(value,i))
        print self.k
        for i in self.k:
            if sum(i) ==S:
                if 0 in i:
                    c+=2**i.count(0)
                else:
                    c+=1

        return c
nums = [0,0,0,0,0,0,0,0,1]
S = 1
print Solution().findTargetSumWays(nums,S)        