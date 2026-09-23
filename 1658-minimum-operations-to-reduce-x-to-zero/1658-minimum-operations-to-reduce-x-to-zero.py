class Solution:
    def minOperations(self, nums, x):
        target = sum(nums) - x
        n = len(nums)

        if target == 0:
            return n

        left = 0
        total = 0
        longest = -1

        for right in range(n):
            total += nums[right]

            while total > target and left <= right:
                total -= nums[left]
                left += 1

            if total == target:
                longest = max(longest, right - left + 1)

        return -1 if longest == -1 else n - longest