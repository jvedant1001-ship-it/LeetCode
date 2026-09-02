class Solution:
    def uniformArray(self, nums1):
        has_even = False
        has_odd = False

        for num in nums1:
            if num % 2 == 0:
                has_even = True
            else:
                has_odd = True

        if not has_even or not has_odd:
            return True

        return True
