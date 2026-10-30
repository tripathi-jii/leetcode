import heapq
from collections import defaultdict
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        if k <= 0:
            return -1

        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))

        if n == 1:
            return 0

        start_count = 1
        if start_count > k:
            return -1

        pq = [(0, 0, labels[0], start_count)]
        dist = {(0, labels[0], start_count): 0}

        while pq:
            cost, node, last_char, count = heapq.heappop(pq)

            state = (node, last_char, count)
            if cost != dist.get(state, float('inf')):
                continue

            if node == n - 1:
                return cost

            for nxt, weight in graph[node]:
                if labels[nxt] == last_char:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count > k:
                    continue

                new_state = (nxt, labels[nxt], new_count)
                new_cost = cost + weight

                if new_cost < dist.get(new_state, float('inf')):
                    dist[new_state] = new_cost
                    heapq.heappush(
                        pq,
                        (new_cost, nxt, labels[nxt], new_count)
                    )

        return -1