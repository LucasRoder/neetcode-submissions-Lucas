class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largestArea = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                if heights[i] < heights[j]:
                    smallestPillar = heights[i];
                else:
                    smallestPillar = heights[j];
                area = smallestPillar * (j-i)

                if area > largestArea:
                    largestArea = area 

        return largestArea                

        