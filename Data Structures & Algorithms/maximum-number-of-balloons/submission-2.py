class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ballon = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}

        for char in text:
            if char in ballon:
                ballon[char] += 1

        ballon["l"] //= 2
        ballon["o"] //= 2

        return min(ballon.values())


 

        

        