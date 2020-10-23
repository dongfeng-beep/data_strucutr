class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range (len(nums)):
            fast = nums[i+1]
            slow = nums[i]
            if fast ==slow:
                for i in  range(i,len(nums)):
                    nums[i] = nums[i+1]
