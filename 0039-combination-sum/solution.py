class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, remaining, path):
            if remaining == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                num = candidates[i]

                if num > remaining:
                    continue

                path.append(num)

                # i (not i + 1) because the same number
                # can be used unlimited times.
                backtrack(i, remaining - num, path)

                path.pop()

        backtrack(0, target, [])
        return result
