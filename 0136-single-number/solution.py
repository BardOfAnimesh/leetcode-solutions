class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=0

        for i in range(len(nums)):
            if i==0:
                x=nums[i]
            else:
                x=x^nums[i]
        return x
