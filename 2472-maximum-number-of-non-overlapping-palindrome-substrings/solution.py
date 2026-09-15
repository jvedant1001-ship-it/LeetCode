class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # pal[l][r] = whether s[l:r+1] is a palindrome
        pal = [[False] * n for _ in range(n)]

        # Build palindrome table by increasing length
        for l in range(n - 1, -1, -1):
            pal[l][l] = True

            for r in range(l + 1, n):
                if s[l] == s[r] and (r - l <= 2 or pal[l + 1][r - 1]):
                    pal[l][r] = True

        # dp[i] = max number of valid palindromes in s[:i]
        dp = [0] * (n + 1)

        for r in range(n):
            # Don't use s[r] in a palindrome
            dp[r + 1] = dp[r]

            # Try every palindrome ending at r
            for l in range(r + 1):
                if r - l + 1 >= k and pal[l][r]:
                    dp[r + 1] = max(dp[r + 1], dp[l] + 1)

        return dp[n]
