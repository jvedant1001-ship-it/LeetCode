class Solution(object):
    def minMoves(self, nums):
        maximum = max(nums)
        moves = 0
        for i in range(len(nums)):
            moves += abs(maximum - nums[i])
        return moves
