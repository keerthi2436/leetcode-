from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)
        a = sorted((l, r, w, i) for i, (l, r, w) in enumerate(intervals))
        starts = [x[0] for x in a]
        nxt = [bisect_right(starts, a[i][1]) for i in range(n)]

        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for k in range(1, 5):
                x = dp[i + 1][k]
                y = dp[nxt[i]][k - 1]
                take = (a[i][2] + y[0], tuple(sorted((a[i][3],) + y[1])))
                dp[i][k] = max(x, take, key=lambda z: (z[0], tuple(-v for v in z[1])))

        return list(dp[0][4][1])