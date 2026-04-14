class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0

        for i in range(len(s)):
            letters = []
            for j in range(i, len(s)):
                if s[j] in letters:
                    break 

                letters.append(s[j])
            if len(letters) > max:
                max = len(letters)
        return max
       