class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        arr = sorted((nums[i], i) for i in range(len(nums)))
        ans = [0] * len(nums)

        i = 0

        while i < len(arr):
            j = i + 1

            while j < len(arr) and arr[j][0] - arr[j - 1][0] <= limit:
                j += 1

            indices = sorted(arr[k][1] for k in range(i, j))

            for k in range(j - i):
                ans[indices[k]] = arr[i + k][0]

            i = j

        return ans