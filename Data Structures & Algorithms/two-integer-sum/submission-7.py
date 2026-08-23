class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #[3,4,5], 7
        seen = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in seen:
                return [seen[compliment], i]
            else:
                seen[nums[i]] = i


