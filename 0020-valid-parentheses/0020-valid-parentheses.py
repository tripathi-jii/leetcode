class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for ch in s:

            if ch in "({[":
                stack.append(ch)

            else:
                if not stack:
                    return False
                
                if stack.pop() != pairs[ch]:
                    return False
            
        return len(stack) == 0
    
        