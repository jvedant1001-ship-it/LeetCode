class Solution:
    def countCommas(self, n):
        ans = 0

        if n >= 1000:
            ans += min(n, 9999) - 1000 + 1

        if n >= 10000:
            ans += (min(n, 99999) - 10000 + 1) * 2

        if n >= 100000:
            ans += (n - 100000 + 1) * 2

        return ans
