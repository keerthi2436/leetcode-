class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)
        size = 1

        while size < n:
            size *= 2

        tree = [(1 % k, [0] * k) for _ in range(2 * size)]

        def make_node(v):
            p = v % k
            cnt = [0] * k
            cnt[p] = 1
            return p, cnt

        def merge(a, b):
            p1, c1 = a
            p2, c2 = b
            cnt = c1[:]

            for r in range(k):
                cnt[(p1 * r) % k] += c2[r]

            return (p1 * p2) % k, cnt

        for i in range(n):
            tree[size + i] = make_node(nums[i])

        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[i * 2], tree[i * 2 + 1])

        def update(pos, val):
            pos += size
            tree[pos] = make_node(val)
            pos //= 2

            while pos:
                tree[pos] = merge(tree[pos * 2], tree[pos * 2 + 1])
                pos //= 2

        def query(l, r):
            left = (1 % k, [0] * k)
            right = (1 % k, [0] * k)

            l += size
            r += size

            while l < r:
                if l & 1:
                    left = merge(left, tree[l])
                    l += 1

                if r & 1:
                    r -= 1
                    right = merge(tree[r], right)

                l //= 2
                r //= 2

            return merge(left, right)

        ans = []

        for index, value, start, x in queries:
            update(index, value)
            result = query(start, n)
            ans.append(result[1][x])

        return ans