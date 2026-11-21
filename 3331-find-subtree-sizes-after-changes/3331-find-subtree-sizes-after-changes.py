
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        last = [-1] * 26

        # Step 1: Find nearest matching ancestors
        stack = [(0, 0, -1)]

        while stack:
            node, state, prev = stack.pop()
            c = ord(s[node]) - ord('a')

            if state == 0:
                prev = last[c]

                if prev != -1:
                    new_parent[node] = prev

                last[c] = node

                stack.append((node, 1, prev))

                for child in reversed(children[node]):
                    stack.append((child, 0, -1))

            else:
                last[c] = prev

        # Step 2: Build the modified tree
        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        # Step 3: Calculate subtree sizes
        order = []
        stack = [0]

        while stack:
            node = stack.pop()
            order.append(node)

            for child in new_children[node]:
                stack.append(child)

        ans = [1] * n

        for node in reversed(order):
            if new_parent[node] != -1:
                ans[new_parent[node]] += ans[node]

        return ans