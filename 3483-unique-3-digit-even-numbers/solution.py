class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        from collections import Counter

        count = Counter(digits)
        ans = 0

        for num in range(100, 1000):
            # Must be even
            if num % 2 != 0:
                continue

            a = num // 100
            b = (num // 10) % 10
            c = num % 10

            needed = Counter([a, b, c])

            # Check if we have enough copies of every digit
            if all(needed[d] <= count[d] for d in needed):
                ans += 1

        return ans
