class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)

        mn = nums.index(min(nums))
        mx = nums.index(max(nums))

        if mn > mx:
            mn, mx = mx, mn

        return min(
            mx + 1,
            n - mn,
            mn + 1 + n - mx
        )