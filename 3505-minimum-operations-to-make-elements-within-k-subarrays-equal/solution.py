
class Solution:
    def minOperations(self, nums, x, k):

        n = len(nums)

        # Coordinate compression
        vals = sorted(set(nums))
        m = len(vals)

        pos = {v: i + 1 for i, v in enumerate(vals)}

        # Fenwick Tree for frequencies and sums
        class BIT:
            def __init__(self, n):
                self.n = n
                self.bit = [0] * (n + 1)

            def add(self, i, val):
                while i <= self.n:
                    self.bit[i] += val
                    i += i & -i

            # Sum of first i positions
            def query(self, i):
                res = 0
                while i > 0:
                    res += self.bit[i]
                    i -= i & -i
                return res

            # Find index of kth smallest element (1-indexed)
            def kth(self, k):
                idx = 0
                step = 1 << (self.n.bit_length() - 1)

                while step:
                    nxt = idx + step

                    if nxt <= self.n and self.bit[nxt] < k:
                        idx = nxt
                        k -= self.bit[nxt]

                    step >>= 1

                return idx + 1

        countBIT = BIT(m)
        sumBIT = BIT(m)

        total_sum = 0

        def update(v, delta):
            nonlocal total_sum

            p = pos[v]

            countBIT.add(p, delta)
            sumBIT.add(p, v * delta)

            total_sum += v * delta

        # Build first window
        for i in range(x):
            update(nums[i], 1)

        costs = []

        # Calculate minimum cost for each window
        for i in range(n - x + 1):

            # Find median
            median_pos = countBIT.kth((x + 1) // 2)
            median = vals[median_pos - 1]

            # Elements strictly smaller than median
            left_count = countBIT.query(median_pos - 1)
            left_sum = sumBIT.query(median_pos - 1)

            # Elements strictly greater than median
            le_count = countBIT.query(median_pos)
            le_sum = sumBIT.query(median_pos)

            right_count = x - le_count
            right_sum = total_sum - le_sum

            # Minimum operations
            cost = (
                median * left_count - left_sum
                + right_sum - median * right_count
            )

            costs.append(cost)

            # Slide window
            if i < n - x:
                update(nums[i], -1)
                update(nums[i + x], 1)

        # Dynamic Programming
        INF = float('inf')

        prev = [0] * (n + 1)

        for j in range(1, k + 1):

            curr = [INF] * (n + 1)

            for i in range(1, n + 1):

                # Skip current element
                curr[i] = curr[i - 1]

                # Choose a window ending at i-1
                if i >= x:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + costs[i - x]
                    )

            prev = curr

        return prev[n]
