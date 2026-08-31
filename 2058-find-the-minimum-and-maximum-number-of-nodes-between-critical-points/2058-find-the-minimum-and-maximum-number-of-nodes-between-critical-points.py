class Solution:
    def nodesBetweenCriticalPoints(self, head):
        vals = []

        while head:
            vals.append(head.val)
            head = head.next

        pos = []

        for i in range(1, len(vals) - 1):
            if (vals[i] > vals[i - 1] and vals[i] > vals[i + 1]) or \
               (vals[i] < vals[i - 1] and vals[i] < vals[i + 1]):
                pos.append(i)

        if len(pos) < 2:
            return [-1, -1]

        mn = min(pos[i] - pos[i - 1] for i in range(1, len(pos)))
        mx = pos[-1] - pos[0]

        return [mn, mx]