class Solution(object):
    def canAliceWin(self, nums):
        single_sum = sum(x for x in nums if x < 10)
        double_sum = sum(x for x in nums if x >= 10)
        
        return single_sum != double_sum