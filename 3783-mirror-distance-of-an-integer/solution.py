
class Solution(object):
    def mirrorDistance(self, n):
        reverse_n = int(str(n)[::-1])
        return abs(n - reverse_n)
