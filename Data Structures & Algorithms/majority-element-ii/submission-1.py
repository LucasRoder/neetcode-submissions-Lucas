class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        amount = []

        for x in range(len(nums)):
            count = 0
            if nums[x] in amount:
                continue
            else:
                for y in range(len(nums)):
                    if nums[x] == nums[y]:
                        count += 1

                if count > len(nums)/3:
                    amount.append(nums[x])

        return amount
        