class Solution(object):
    def minMoves2(self, nums):
        n = len(nums)
        nums.sort()
        if (n) % 2 == 0:
            median = (nums[n // 2 - 1] + nums[n // 2]) / 2
        else:
            median = nums[n // 2]
        moves = 0 
        for i in range(n):
            moves += abs(nums[i] - median)
        return moves
        """
        :type nums: List[int]
        :rtype: int
        """
