from typing import List

class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0
        stack = [(0, -1, 0)]

        while stack:
            u, p, state = stack.pop()

            if state == 0:
                parent[u] = u if p == -1 else p
                tin[u] = timer
                timer += 1
                stack.append((u, p, 1))

                for v in reversed(graph[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer - 1

        LOG = n.bit_length()
        up = [parent[:]]

        for j in range(1, LOG):
            prev = up[j - 1]
            up.append([prev[prev[i]] for i in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]

            for j in range(LOG):
                if diff & (1 << j):
                    u = up[j][u]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return parent[u]

        bit = [0] * (n + 2)

        def add(i, val):
            i += 1
            while i < len(bit):
                bit[i] ^= val
                i += i & -i

        def point_query(i):
            i += 1
            result = 0

            while i > 0:
                result ^= bit[i]
                i -= i & -i

            return result

        def range_xor(left, right, val):
            add(left, val)
            add(right + 1, val)

        chars = list(s)
        base = [0] * n

        for u in sorted(range(n), key=lambda x: depth[x]):
            mask = 1 << (ord(chars[u]) - ord('a'))
            base[u] = mask if parent[u] == u else base[parent[u]] ^ mask

        answer = []

        for query in queries:
            parts = query.split()
            u = int(parts[1])

            if parts[0] == "update":
                c = parts[2]
                old_mask = 1 << (ord(chars[u]) - ord('a'))
                new_mask = 1 << (ord(c) - ord('a'))

                if old_mask != new_mask:
                    range_xor(tin[u], tout[u], old_mask ^ new_mask)
                    chars[u] = c
            else:
                v = int(parts[2])
                ancestor = lca(u, v)

                mask_u = base[u] ^ point_query(tin[u])
                mask_v = base[v] ^ point_query(tin[v])

                path_mask = mask_u ^ mask_v ^ (
                    1 << (ord(chars[ancestor]) - ord('a'))
                )

                answer.append((path_mask & (path_mask - 1)) == 0)

        return answer