class Solution(object):
    def longestMonotonicSubarray(self, nums):
        n = len(nums)
        ans = 0
        inc = 1
        dec = 1

        for i in range(1,n):
            if nums[i]>nums[i-1]:
                inc += 1
                dec = 1
            elif nums[i]<nums[i-1]:
                dec += 1
                inc = 1
            else:
                inc = 1
                dec = 1
            ans = max(inc , dec)
        return ans

        """
        :type nums: List[int]
        :rtype: int
        """
