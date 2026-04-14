class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for y in range(len(nums)):
            for x in range(len(nums)-1):
                if nums[x] > nums[x+1]:
                    temp = nums[x+1]
                    nums[x+1] = nums[x]
                    nums[x] = temp

