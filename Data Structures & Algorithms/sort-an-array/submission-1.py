class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        output = []

        for y in range(len(nums)):
            smallest = min(nums)
            output.append(smallest)
            nums.remove(smallest)

        return output





        