class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_t = {}
        letter_s = {}
        
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            current_s = s[i]
            if current_s in letter_s:
                letter_s[current_s] += 1
            else:
                letter_s[current_s] = 1

        for i in range(len(t)):
            current_t = t[i]
            if current_t in letter_t:
                letter_t[current_t] +=1
            else:
                letter_t[current_t] = 1

        if letter_s == letter_t:
            return True
        else:
            return False




            