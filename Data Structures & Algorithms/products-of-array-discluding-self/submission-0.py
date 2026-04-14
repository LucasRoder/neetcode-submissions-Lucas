class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            tempList = nums[:]
            tempList.pop(i)
            tempNum = 1
            for y in range(len(tempList)):
                tempNum *= tempList[y]
            output.append(tempNum)

        return output

        