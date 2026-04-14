class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) > len(word2):
            smallest = word2
            largest = word1
        else:
            smallest = word1
            largest = word2


        output = ""
        for i in range(len(smallest)):
            output += word1[i]
            output += word2[i]

        output += largest[i+1:]

        return output

