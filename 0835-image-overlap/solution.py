class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)

        ones1 = []
        ones2 = []

        for r in range(n):
            for c in range(n):
                if img1[r][c]:
                    ones1.append((r, c))
                if img2[r][c]:
                    ones2.append((r, c))

        shifts = {}
        ans = 0

        for r1, c1 in ones1:
            for r2, c2 in ones2:
                shift = (r2 - r1, c2 - c1)

                shifts[shift] = shifts.get(shift, 0) + 1
                ans = max(ans, shifts[shift])

        return ans
