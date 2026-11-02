class Solution:
    def largestGoodInteger(self, num: str) -> str:
        output = []
        good = []

        for n in num:
            if n in good:
                good.append(n)
                if len(good) == 3:
                    output.append("".join(good))
            else:
                good.clear()
                good.append(n)
        
        if len(output) != 0:
            return str(max(output))
        else:
            return ""
