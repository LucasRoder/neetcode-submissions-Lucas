class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        half = float(len(nums)) / 2

        count = 0
        for x in range(len(nums)):
            for y in range(len(nums)):
                if nums[x] == nums[y]:
                    count += 1

            if count >= half:
                return nums[x]
            count = 0
                


        