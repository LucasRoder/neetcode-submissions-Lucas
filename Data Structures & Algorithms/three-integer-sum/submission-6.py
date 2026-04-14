class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                for z in range(y+1, len(nums)):
                    subList = []
                    if x!= y and y != z and z!= x and nums[x]+nums[y]+nums[z] == 0:
                        subList.append(nums[x])
                        subList.append(nums[y])
                        subList.append(nums[z])
                        subList.sort()
                        if subList not in output and subList != []:
                            output.append(subList)

                    

        return output
                


        