class Solution:
    def isValid(self, s: str) -> bool:
        
        parens = {
            '}':'{',
            ']':'[',
            ')':'('
        }

        my_stack = []

        for p in s:
            if p in parens:
                if my_stack and my_stack[-1] == parens[p]:
                    my_stack.pop()
                else:
                    return False
            else:
                my_stack.append(p)

        return not my_stack