class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0

        for i, ch in enumerate(s):
            value = ord(ch) - ord('a') + 1
            reverse = 27 - value
            ans += reverse * (i + 1)

        return ans