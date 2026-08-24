class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest=nums[0]+nums[1]+nums[2]

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left<right:
                sum = nums[i]+ nums[left]+ nums[right]
                if abs(sum-target)< abs(closest - target):
                    closest = sum
                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1          
                else:
                    return sum
        return closest        