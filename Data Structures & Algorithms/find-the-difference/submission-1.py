class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sMap = {}
        for char in s:
            if char in sMap:
                sMap[char] += 1
            else:
                sMap[char] = 1


        for char in t:
            if char not in sMap:
                return char
            else:
                if sMap[char] == 0:
                    return char
                else:
                    sMap[char] -= 1
                 

        