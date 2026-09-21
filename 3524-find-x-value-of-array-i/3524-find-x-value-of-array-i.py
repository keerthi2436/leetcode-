class Solution:
    def resultArray(self, nums, k):
        ans = [0] * k
        cur = [0] * k

        for x in nums:
            nxt = [0] * k
            nxt[x % k] += 1

            for r in range(k):
                nxt[(r * x) % k] += cur[r]

            cur = nxt

            for r in range(k):
                ans[r] += cur[r]

        return ans