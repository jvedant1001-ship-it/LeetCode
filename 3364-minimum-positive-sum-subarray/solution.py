class Solution:
    def minimumSumSubarray(self, nums, l, r):

        n = len(nums)
        prefix = [0]

        for num in nums:
            prefix.append(prefix[-1] + num)

        ans = float('inf')

        for i in range(n):
            for j in range(l, r + 1):
                if i + j <= n:
                    s = prefix[i + j] - prefix[i]

                    if s > 0:
                        ans = min(ans, s)

        return ans if ans != float('inf') else -1
