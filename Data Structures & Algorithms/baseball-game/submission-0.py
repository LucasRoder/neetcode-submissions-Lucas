class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        specailOperations = {"+", "D", "C"}
        for operation in operations:
            if operation not in specailOperations:
                stack.append(int(operation))
            else:
                if operation == "+":
                    stack.append(stack[-2] + stack[-1])
                elif operation == "D":
                    stack.append(stack[-1] * 2)
                elif  operation == "C":
                    stack.pop()
        return sum(stack)

        