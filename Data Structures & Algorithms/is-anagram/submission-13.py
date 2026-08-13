class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = {}
        t_letters = {}
        for i in range(len(s)):
            letter = s[i]
            if letter in s_letters:
                s_letters[letter] += 1
            else:
                s_letters[letter] = 1

        for i in range(len(t)):
                letter = t[i]
                if letter in t_letters:
                    t_letters[letter] += 1
                else:
                    t_letters[letter] = 1
        return s_letters == t_letters



            