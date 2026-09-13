class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)
        a = [(i, j) for i in range(n) for j in range(n) if img1[i][j]]
        b = [(i, j) for i in range(n) for j in range(n) if img2[i][j]]

        count = {}

        for i, j in a:
            for x, y in b:
                shift = (i - x, j - y)
                count[shift] = count.get(shift, 0) + 1

        return max(count.values(), default=0)