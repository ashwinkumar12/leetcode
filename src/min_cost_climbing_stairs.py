class Solution(object):
    def __init__(self):
        self.min_cost_dict = dict()
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.append(0)
        cost_1 = self.cost_min(cost)    
        #cost_2 = self.cost_min(cost[1:])
        #print cost,cost_1
        #print cost[1:],cost_2
        #return min(cost_1, cost_2)
        return cost_1
    
    def cost_min(self,cost):
        if len(cost)-1 in self.min_cost_dict:
            return self.min_cost_dict[len(cost)-1]
        if not cost:
            return 0
        #print cost
        cost_1 = self.cost_min(cost[:-1])
        #print 'cost_1 ',cost[:-1],cost_1
        cost_2 = self.cost_min(cost[:-2])
        #print 'cost_2 ',cost[:-2],cost_2
                
        self.min_cost_dict[len(cost)-1] = cost[-1] + min(cost_1,cost_2)
        return self.min_cost_dict[len(cost)-1]


cost = [1,10,1,2]

a = Solution()
print a.minCostClimbingStairs(cost)
print a.min_cost_dict

"""
class Solution(object):
    def __init__(self):
        self.min_cost_dict = dict()
    def minCostClimbingStairs(self, cost):
        cost.append(0)
        min_cost = self.cost_min(cost)    
        return min_cost
    
    def cost_min(self,cost):
        if len(cost)-1 in self.min_cost_dict:
            return self.min_cost_dict[len(cost)-1]
        if not cost:
            return 0
        self.min_cost_dict[len(cost)-1] = cost[-1] + min(self.cost_min(cost[:-1]),self.cost_min(cost[:-2]))
        return self.min_cost_dict[len(cost)-1]
"""
