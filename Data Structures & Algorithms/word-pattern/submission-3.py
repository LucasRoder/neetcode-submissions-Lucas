class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sList = s.split()
        patternMap = {}
        sListMap = {}

        if len(pattern) != len(sList):
            return False

        for i in range(len(pattern)):
            if pattern[i] in patternMap:
                if patternMap[pattern[i]]!= sList[i]:
                    return False
            if sList[i] in sListMap:
                if sListMap[sList[i]] != pattern[i]:
                    return False
            else:
                    patternMap[pattern[i]] = sList[i]
                    sListMap[sList[i]] = pattern[i]

        return True

                



        