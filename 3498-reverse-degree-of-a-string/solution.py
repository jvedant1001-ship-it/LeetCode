class Solution:
    def reverseDegree(self, s):
        total = 0

        for i, ch in enumerate(s, start=1):
            # 'a' -> 26, 'b' -> 25, ..., 'z' -> 1
            reverse_value = ord('z') - ord(ch) + 1
            total += reverse_value * i

        return total
