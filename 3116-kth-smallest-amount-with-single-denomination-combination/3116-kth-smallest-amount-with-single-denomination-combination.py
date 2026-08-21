from math import gcd

class Solution:
    def findKthSmallest(self, coins, k):
        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            total = 0
            n = len(coins)

            # Inclusion-exclusion
            for mask in range(1, 1 << n):
                bits = 0
                multiple = 1
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        multiple = lcm(multiple, coins[i])

                        if multiple > x:
                            valid = False
                            break

                if not valid:
                    continue

                if bits % 2 == 1:
                    total += x // multiple
                else:
                    total -= x // multiple

            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left