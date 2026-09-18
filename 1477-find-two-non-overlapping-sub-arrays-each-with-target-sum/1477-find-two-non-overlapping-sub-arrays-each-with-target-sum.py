class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = n + 1
        dp = [INF] * (n + 1)
        pos = {0: 0}
        prefix = 0
        ans = INF

        for i in range(1, n + 1):
            prefix += arr[i - 1]
            dp[i] = dp[i - 1]

            if prefix - target in pos:
                j = pos[prefix - target]
                length = i - j

                if dp[j] != INF:
                    ans = min(ans, length + dp[j])

                dp[i] = min(dp[i], length)

            pos[prefix] = i

        return -1 if ans == INF else ans