class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        from collections import Counter

        cnt = Counter(s)
        n = len(s)

        i = 0
        while i < n and cnt[target[i]] > 0:
            cnt[target[i]] -= 1
            i += 1

        j = i

        while j >= 0:
            if j < i:
                cnt[target[j]] += 1

            if j < n:
                for c in range(ord(target[j]) + 1, ord('z') + 1):
                    ch = chr(c)

                    if cnt[ch] > 0:
                        cnt[ch] -= 1

                        ans = target[:j] + ch

                        for x in range(ord('a'), ord('z') + 1):
                            ans += chr(x) * cnt[chr(x)]

                        return ans

            j -= 1

        return ""