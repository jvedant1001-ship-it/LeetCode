
from sortedcontainers import SortedList

class Solution:
    def minOperations(self, nums, x, k):

        n = len(nums)
        window = SortedList()
        window_sum = 0

        costs = []

        # Build the first window
        for i in range(x):
            window.add(nums[i])
            window_sum += nums[i]

        # Calculate cost using median
        for i in range(n - x + 1):

            median = window[x // 2]

            left_sum = sum(window[:x // 2])
            right_sum = sum(window[x // 2 + 1:])

            left_count = x // 2
            right_count = x - left_count - 1

            cost = (
                median * left_count - left_sum
                + right_sum - median * right_count
            )

            costs.append(cost)

            if i == n - x:
                break

            # Remove outgoing element
            window.remove(nums[i])

            # Add incoming element
            window.add(nums[i + x])

        # DP
        INF = float('inf')

        prev = [0] * (n + 1)

        for j in range(1, k + 1):

            curr = [INF] * (n + 1)

            for i in range(1, n + 1):

                # Skip current element
                curr[i] = curr[i - 1]

                # Select a subarray of size x
                if i >= x:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + costs[i - x]
                    )

            prev = curr

        return prev[n]
