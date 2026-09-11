class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        s = set()

        n = len(digits)

        for i in range(n):          # units
            if digits[i] % 2 != 0:
                continue

            for j in range(n):      # tens
                if j == i:
                    continue

                for k in range(n):  # hundreds
                    if k == i or k == j or digits[k] == 0:
                        continue

                    num = digits[k] * 100 + digits[j] * 10 + digits[i]
                    s.add(num)

        return len(s)