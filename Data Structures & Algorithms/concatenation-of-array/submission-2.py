class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        numsCopy = nums[:]
        numsCopy.extend(nums)

        return numsCopy