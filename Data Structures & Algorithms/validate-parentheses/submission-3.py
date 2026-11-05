class Solution:
    def isValid(self, s: str) -> bool:
       
        opener={"{":"}",
                "[":"]",
                "(":")",
                ".":"."}
        stack=["."]
        for bracket in s:
            if bracket in opener:
                stack.append(bracket)
            else:
                if bracket==opener[stack[-1]]:
                    del stack[-1]
                else:
                    return False
            
        return True if len(stack)==1 else False