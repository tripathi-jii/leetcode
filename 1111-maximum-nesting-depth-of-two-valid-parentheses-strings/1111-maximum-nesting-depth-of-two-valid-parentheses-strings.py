class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        answer = []
        depth = 0

        for ch in seq:
            if ch == '(':
                depth += 1

            answer.append(depth % 2)

            if ch == ')':
                depth -= 1

        return answer