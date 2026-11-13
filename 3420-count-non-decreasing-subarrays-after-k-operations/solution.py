class Solution(object):
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)

        # Prefix sums
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        # Next greater element to the right
        ng = [n] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            if stack:
                ng[i] = stack[-1]

            stack.append(i)

        # Binary lifting tables
        LOG = n.bit_length()

        jump = [ng]
        sums = [[nums[i] * (ng[i] - i) for i in range(n)]]

        for p in range(1, LOG):
            prev_jump = jump[-1]
            prev_sum = sums[-1]

            curr_jump = [n] * n
            curr_sum = [0] * n

            for i in range(n):
                mid = prev_jump[i]

                if mid < n:
                    curr_jump[i] = prev_jump[mid]
                    curr_sum[i] = prev_sum[i] + prev_sum[mid]
                else:
                    curr_sum[i] = prev_sum[i]

            jump.append(curr_jump)
            sums.append(curr_sum)

        # Minimum operations for nums[l:r+1]
        def cost(l, r):
            total = 0
            cur = l

            for p in range(LOG - 1, -1, -1):
                nxt = jump[p][cur]

                if nxt <= r:
                    total += sums[p][cur]
                    cur = nxt

            total += nums[cur] * (r - cur + 1)

            return total - (pref[r + 1] - pref[l])

        ans = 0

        # Binary search for the smallest valid left boundary
        for r in range(n):
            low, high = 0, r

            while low < high:
                mid = (low + high) // 2

                if cost(mid, r) <= k:
                    high = mid
                else:
                    low = mid + 1

            ans += r - low + 1

        return ans
