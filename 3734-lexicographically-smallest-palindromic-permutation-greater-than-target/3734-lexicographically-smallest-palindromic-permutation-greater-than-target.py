class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = [0] * 26

        for c in s:
            cnt[ord(c) - 97] += 1

        mid = ""

        for i in range(26):
            if cnt[i] % 2:
                if mid:
                    return ""
                mid = chr(i + 97)
                cnt[i] -= 1

        for i in range(n // 2):
            cnt[ord(target[i]) - 97] -= 2

        def valid():
            for x in cnt:
                if x < 0:
                    return False
            return True

        if valid():
            left = target[:n // 2]
            right = mid + left[::-1]

            if right > target[n // 2:]:
                return left + right

        for i in range(n // 2 - 1, -1, -1):
            x = ord(target[i]) - 97
            cnt[x] += 2

            if not valid():
                continue

            for y in range(x + 1, 26):
                if cnt[y] >= 2:
                    cnt[y] -= 2

                    left = target[:i] + chr(y + 97)

                    for j in range(26):
                        left += chr(j + 97) * (cnt[j] // 2)

                    return left + mid + left[::-1]

        return ""