class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l=len(nums)-1
        r=0
        count=0
        while r<len(nums):
            if  l <= r:
                if l<r:
                    break
                elif nums[r]!=val:
                    count += 1
                    break
                else:
                    break
            elif nums[l]==val:
                l-=1
                r+=0
            elif nums[r]==val and nums[l]!=val:

                nums[r]=nums[l]
                l-=1
                r+=1
                count+=1
            
            else:
                r+=1
                count+=1
        return count

