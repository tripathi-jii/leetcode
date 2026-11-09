
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:

        count = [0] * k
        size = 1

        while size < k:
            size *= 2

        tree = [0] * (2 * size)

        for i in range(k):
            tree[size + i] = 1

        for i in range(size - 1, 0, -1):
            tree[i] = tree[2 * i] + tree[2 * i + 1]

        def update(pos, val):
            pos += size
            tree[pos] = val

            while pos > 1:
                pos //= 2
                tree[pos] = tree[2 * pos] + tree[2 * pos + 1]

        def find_first(node, left, right, ql, qr):
            if right < ql or left > qr or tree[node] == 0:
                return -1

            if left == right:
                return left

            mid = (left + right) // 2

            res = find_first(2 * node, left, mid, ql, qr)

            if res != -1:
                return res

            return find_first(2 * node + 1, mid + 1, right, ql, qr)

        busy = []

        for i in range(len(arrival)):

            while busy and busy[0][0] <= arrival[i]:
                end, server = heapq.heappop(busy)
                update(server, 1)

            start = i % k

            server = find_first(1, 0, size - 1, start, k - 1)

            if server == -1:
                server = find_first(1, 0, size - 1, 0, start - 1)

            if server == -1:
                continue

            count[server] += 1
            update(server, 0)

            heapq.heappush(
                busy,
                (arrival[i] + load[i], server)
            )

        maximum = max(count)

        return [i for i in range(k) if count[i] == maximum]
