from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m, n = len(classroom), len(classroom[0])

        litter = {}
        sx = sy = 0
        k = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    sx, sy = i, j
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = k
                    k += 1

        if k == 0:
            return 0

        full = (1 << k) - 1
        q = deque([(sx, sy, energy, full)])
        vis = {(sx, sy, energy, full)}

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        moves = 0

        while q:
            for _ in range(len(q)):
                x, y, e, mask = q.popleft()

                if mask == 0:
                    return moves

                if e == 0:
                    continue

                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy

                    if not (0 <= nx < m and 0 <= ny < n):
                        continue

                    if classroom[nx][ny] == 'X':
                        continue

                    ne = e - 1
                    nm = mask

                    if classroom[nx][ny] == 'R':
                        ne = energy

                    if (nx, ny) in litter:
                        nm &= ~(1 << litter[(nx, ny)])

                    state = (nx, ny, ne, nm)

                    if state not in vis:
                        vis.add(state)
                        q.append(state)

            moves += 1

        return -1