from pprint import pprint
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if len(nums) == 1 and S==nums[0] or S==-nums[0]:
            return 1
            
        v = nums
        rs = [v[0],-v[0]]
        final = []
        for i in v[1:]:
            #print i
            pm = [i,-i]
            #print rs,pm
            for m in rs:
                for n in pm:
                    if isinstance(m,list):
                        final.append(m+[n])
                    else:
                        final.append([m,n])
            #print final
            if len(final) == 2**len(v):
                break
            rs = final
            final = []
        count = 0
        #pprint(final)
        #print len(final)
        for i in final:
            if sum(i) == S:
                count +=1
        return count

nums = [0,0,0,0,0,0,0,0,1]
S = 0
print Solution().findTargetSumWays(nums,S)