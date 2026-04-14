class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        tempPrefix = ""
        subString = 1
        base = strs[0]

        while subString <= len(base):
            correct = True
            for y in strs:
                if base[0:subString] != y[0:subString]:
                    correct = False

            if correct == True:
                tempPrefix = base[0:subString]
                subString += 1
            else:
                return tempPrefix
        return tempPrefix

            



        