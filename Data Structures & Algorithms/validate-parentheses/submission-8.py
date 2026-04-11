class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        parens = {
            ']':'[',
            '}':'{',
            ')':'('
        }

        for c in s:
            # Check if c is a closing parentheses
            if c in parens:
                # Check if we have a stack and check if top of stack is
                # the corresponding value. IF it is, we pop it.
                if stack and stack[-1] == parens[c]:
                    stack.pop()
                else:
                    return False
            # Else, append
            else:
                stack.append(c)

        return not stack