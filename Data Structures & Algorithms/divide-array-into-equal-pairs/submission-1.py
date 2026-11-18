class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        numsMap = {}

        for num in nums:
            if num in numsMap:
                numsMap[num] += 1
            else:
                numsMap[num] = 1


        for num in numsMap:
            if numsMap[num] % 2 != 0:
                return False
        return True

        