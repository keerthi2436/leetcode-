class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)

        # Prefix sums
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        # dp[i][j] = maximum score for stoneValue[i:j+1]
        dp = [[-1] * n for _ in range(n)]

        def dfs(i, j):
            if i >= j:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            ans = 0
            left = 0
            right = prefix[j + 1] - prefix[i]

            for k in range(i, j):

                left += stoneValue[k]
                right -= stoneValue[k]

                if left < right:

                    # Maximum possible score from this choice
                    # cannot beat ans
                    if ans >= 2 * left:
                        continue

                    ans = max(ans, left + dfs(i, k))

                elif left > right:

                    if ans >= 2 * right:
                        break

                    ans = max(ans, right + dfs(k + 1, j))

                else:
                    ans = max(
                        ans,
                        left + dfs(i, k),
                        right + dfs(k + 1, j)
                    )

            dp[i][j] = ans
            return ans

        return dfs(0, n - 1)