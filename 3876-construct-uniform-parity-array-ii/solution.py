class Solution:
    def uniformArray(self, nums1):
        min_odd = float('inf')
        min_even = float('inf')

        for x in nums1:
            if x % 2:
                min_odd = min(min_odd, x)
            else:
                min_even = min(min_even, x)

        # All numbers have the same parity
        if min_odd == float('inf') or min_even == float('inf'):
            return True

        # We can make every even number odd by subtracting
        # the smallest odd number.
        return min_odd < min_even
