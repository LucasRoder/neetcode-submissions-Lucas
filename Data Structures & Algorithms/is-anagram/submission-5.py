class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        tList = []
        for j in t:
            tList.append(j)

        sList = []
        for i in s:
            sList.append(i)
            if i in tList:
                tList.remove(i)
                sList.remove(i)


        if len(sList) > 0:
            return False
        else:
            return True