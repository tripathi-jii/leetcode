import heapq
from typing import List

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)

        busy = []
        ans = []

        time = 0

        for j, task in enumerate(tasks):
            time = max(time, j)

            if not free and busy:
                time = max(time, busy[0][0])

            while busy and busy[0][0] <= time:
                end_time, weight, idx = heapq.heappop(busy)
                heapq.heappush(free, (weight, idx))

            weight, idx = heapq.heappop(free)
            ans.append(idx)

            heapq.heappush(busy, (time + task, weight, idx))

        return ans