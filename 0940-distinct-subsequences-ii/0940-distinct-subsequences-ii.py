class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = 1
        last = {}

        for i, ch in enumerate(s):
            new = dp * 2 % MOD

            if ch in last:
                new = (new - last[ch]) % MOD

            last[ch] = dp
            dp = new

        return (dp - 1) % MOD