class Solution:
    def isValid(self, s: str) -> bool:
        
        c_o = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }

        my_stack = []

        for v in s:
            if v in c_o:
                if my_stack and my_stack[-1] == c_o[v]:
                    my_stack.pop()
                else:
                    return False
            else:
                my_stack.append(v)

        return not my_stack