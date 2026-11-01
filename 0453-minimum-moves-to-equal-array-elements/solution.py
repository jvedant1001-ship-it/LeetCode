class Solution(object):
    def minMoves(self, nums):
        minimum = min(nums)
        move=0
        for i in range(len(nums)):
            move += nums[i] - minimum
                
        return move


        """
        :type nums: List[int]
        :rtype: int
        """
