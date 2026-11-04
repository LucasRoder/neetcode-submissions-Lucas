class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky = -1
        numsMap = {}
        for num in arr:
            if num in numsMap:
                numsMap[num] += 1
            else:
                numsMap[num] = 1

        for num in numsMap:
            if num == numsMap[num]:
                if lucky < num:
                    lucky = num
        
        return lucky
