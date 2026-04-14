class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0

        nums.sort()

        for x in range(len(nums)):
            tempCount = 1
            for y in range(len(nums)):
                if nums[x] == (nums[y] - tempCount):
                    tempCount += 1

            if tempCount > count:
                count = tempCount

        return count

        