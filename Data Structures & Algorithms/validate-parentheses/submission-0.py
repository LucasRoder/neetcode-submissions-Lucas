class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in close:
                if len(stack) == 0:
                    return False
                if stack[-1] == close[char]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(char)


        if len(stack) != 0:
            return False
        else:
            return True

        