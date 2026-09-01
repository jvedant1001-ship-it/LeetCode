from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        start = None
        litter_id = {}

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter_id[(r, c)] = len(litter_id)

        k = len(litter_id)

        # No litter
        if k == 0:
            return 0

        full_mask = (1 << k) - 1

        # visited[(r, c, mask)] = maximum energy remaining
        #
        # Instead of a set containing energy as another dimension,
        # keep only the best energy for each (r, c, mask).
        best = {}

        sr, sc = start
        best[(sr, sc, 0)] = energy

        q = deque()
        q.append((sr, sc, 0, energy))

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        moves = 0

        while q:
            for _ in range(len(q)):
                r, c, mask, e = q.popleft()

                if mask == full_mask:
                    return moves

                if e == 0:
                    continue

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    new_e = e - 1
                    new_mask = mask

                    # Collect litter
                    if classroom[nr][nc] == 'L':
                        bit = litter_id[(nr, nc)]
                        new_mask |= 1 << bit

                    # Reset energy
                    if classroom[nr][nc] == 'R':
                        new_e = energy

                    # If we already reached this state with >= energy,
                    # this state is useless.
                    key = (nr, nc, new_mask)

                    if new_e <= best.get(key, -1):
                        continue

                    best[key] = new_e
                    q.append((nr, nc, new_mask, new_e))

            moves += 1

        return -1
