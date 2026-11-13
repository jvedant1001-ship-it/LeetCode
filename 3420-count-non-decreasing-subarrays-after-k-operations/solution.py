
class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)
        stack = []
        left = 0
        ans = 0
        cost = 0

        for right in range(n):
            while stack and nums[stack[-1]] <= nums[right]:
                idx = stack.pop()

                prev = stack[-1] if stack else left - 1

                cost -= nums[idx] * (idx - prev)

            prev = stack[-1] if stack else left - 1

            cost += nums[right] * (right - prev)

            stack.append(right)

            while cost > k:
                if stack and stack[0] == left:
                    stack.pop(0)

                left += 1

                cost = 0
                prev = left - 1

                for idx in stack:
                    cost += nums[idx] * (idx - prev)
                    prev = idx

            ans += right - left + 1

        return ans
