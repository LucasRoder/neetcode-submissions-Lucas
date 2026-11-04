class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedHieghts = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if sortedHieghts[i] != heights[i]:
                count += 1
        return count
        