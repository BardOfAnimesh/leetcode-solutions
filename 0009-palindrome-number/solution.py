class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a= list(str(x))
        valid = True
        for i in range(len(a)//2):
            if a[i]==a[len(a)-i-1]:
                continue
            else:
               valid = False
               break
        return valid

