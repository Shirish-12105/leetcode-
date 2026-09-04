class Solution(object):
    def firstStableIndex(self, nums, k):
        for i in range(len(nums)):
            left = nums[:i+1]
            right = nums[i:]

            score = max(left)-min(right)

            if score <= k:
                 return i
        return -1        