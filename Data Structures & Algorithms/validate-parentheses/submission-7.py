class Solution:
    def isValid(self, s: str) -> bool:
        

        my_stack = []
        parens = {
            '}':'{',
            ']':'[',
            ')':'('
        }

        for c in s:
            if c in parens:
                if my_stack and my_stack[-1] == parens[c]:
                    my_stack.pop()
                else:
                    return False
            else:
                my_stack.append(c)

        return not my_stack