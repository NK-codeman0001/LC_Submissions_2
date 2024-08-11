import itertools

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        for i in range(0,l):
            for j in range(i+1,l):
                s = nums[i]+nums[j]
                if target == s:
                    return [i,j]
                
        return [0,0]
        