class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        smallestNum = 1
        while True:
            if smallestNum in nums:
                smallestNum +=1
            else:
                return smallestNum

        