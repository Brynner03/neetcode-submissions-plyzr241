class Solution:
    def isValid(self, s: str) -> bool:
        
        close_to_open = {
            ']':'[',
            '}':'{',
            ')':'('
        }

        my_stack = []

        for p in s:
            if p in close_to_open:
                if (my_stack and my_stack[-1] == close_to_open[p]):
                    my_stack.pop()
                else:
                    return False
            else:
                my_stack.append(p)
        
        return not my_stack