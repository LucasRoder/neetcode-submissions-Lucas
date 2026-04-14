class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for x in range(len(nums)):
            for y in range(len(nums)):
                if x != y and nums[x] == nums[y]:
                    nums[y] = 'x'

        while 'x' in nums:
            nums.remove('x')


        return len(nums)
        