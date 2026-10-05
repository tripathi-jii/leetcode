class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                value = stack.pop()

                if value == 0:
                    value = 1
                else:
                    value = 2 * value

                stack[-1] += value

        return stack[0]