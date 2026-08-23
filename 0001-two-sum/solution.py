class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}
        for i in range(len(nums)):
            a= target - nums[i]
            if a in seen:
                return[seen[a],i]
            seen[nums[i]]=i
