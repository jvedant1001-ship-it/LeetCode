class Solution(object):
    def digitFrequencyScore(self, n):
        freq = {}

        for digit in str(n):
            freq[digit] = freq.get(digit, 0) + 1

        score = 0

        for digit, count in freq.items():
            score += int(digit) * count

        return score
