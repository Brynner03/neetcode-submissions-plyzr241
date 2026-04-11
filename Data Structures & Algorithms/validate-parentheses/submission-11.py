class Solution:
    def isValid(self, s: str) -> bool:

        close_to_open = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }
        my_stack = []

        for val in s:
            if val in close_to_open:
                if my_stack and my_stack[-1] == close_to_open[val]:
                    my_stack.pop()
                else:
                    return False
            else:
                my_stack.append(val)

        return not my_stack