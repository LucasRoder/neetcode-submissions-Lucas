class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output = []
        for x in range(len(numbers)):
            for y in range(x,len(numbers)):
                if x!= y and numbers[x]+numbers[y] == target:
                    output.append(x+1)
                    output.append(y+1)

        return output
