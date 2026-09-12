from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)
        a = sorted((l, r, w, i) for i, (l, r, w) in enumerate(intervals))

        # next[i] = first interval whose left endpoint > a[i].right
        starts = [x[0] for x in a]
        nxt = [bisect_right(starts, a[i][1]) for i in range(n)]

        # dp[k][i] = best (score, indices) using at most k intervals from i onward.
        dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]

        for k in range(1, 5):
            for i in range(n - 1, -1, -1):
                skip = dp[k][i + 1]

                score, ids = dp[k - 1][nxt[i]]
                take = (score + a[i][2], ids + (a[i][3],))

                # Compare by maximum score, then lexicographically smallest indices.
                if take[0] > skip[0] or (
                    take[0] == skip[0] and tuple(sorted(take[1])) < tuple(sorted(skip[1]))
                ):
                    dp[k][i] = take
                else:
                    dp[k][i] = skip

        return list(sorted(dp[4][0][1]))
