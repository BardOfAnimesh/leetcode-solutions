class Solution(object):
    def minimumSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        l=0
        r=len(nums)-1
        swaps=0
        while(l < r):
            if nums[l]==0 and nums[r]!=0:
                nums[l]=nums[r]
                nums[r]=0
                l+=1
                r-=1
                swaps+=1
            elif nums[r]==0:
                r-=1
            elif nums[l]!=0:
                l+=1
            else:
                break
            
        return swaps
