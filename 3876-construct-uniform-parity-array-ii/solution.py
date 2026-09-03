class Solution:
    def constructUniformParityArray(self, nums1):
        min_odd = float('inf')
        min_even = float('inf')

        for x in nums1:
            if x % 2:
                min_odd = min(min_odd, x)
            else:
                min_even = min(min_even, x)

        # Already uniform parity
        if min_odd == float('inf') or min_even == float('inf'):
            return True

        # Make everything odd:
        # every even x needs a smaller odd number.
        can_make_odd = all(
            x % 2 == 1 or x > min_odd
            for x in nums1
        )

        # Make everything even:
        # every odd x needs a smaller even number.
        can_make_even = all(
            x % 2 == 0 or x > min_even
            for x in nums1
        )

        return can_make_odd or can_make_even
