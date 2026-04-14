class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        fullList = []
        for char in s:
            if char.isalnum():
                fullList.append(char)

        for i in range (len(fullList)//2):
            if fullList[i] != fullList[len(fullList)-1-i]:
                return False

        return True
