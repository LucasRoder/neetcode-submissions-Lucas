class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []

        for i in strs:
            sublist = []
            for j in strs:
                if sorted(i) == sorted(j):
                    sublist.append(j)
            if sublist not in output:
                output.append(sublist)

        return output